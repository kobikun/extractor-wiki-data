#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""extract wiki data program"""
__author__ = "byeongil ko"
__email__ = "byeongil.ko(at)gmail(dot)com"
__date__ = "creation: 2016-07-05"
__copyright__ = "All Rights Reserved by kobi"


###########
# imports #
###########
import argparse
import logging
import sys
import json
import HTMLParser


############
# constant #
############
# language class
CN_LIST=['en','ja','zh','ko','fr','ar','de','es', 'tr', 'vi', 'pt', 'ru']
WIKI_LIST= [ '%swiki' % x for x in CN_LIST]
# key list(type)
KEY_LIST=['sitelinks', 'labels', 'descriptions', 'claims', 'aliases']

def print_dict (ddict,step=1):
  """
  print dict data
  """
  for k,v in ddict.iteritems():
    print " "*step, k
    if isinstance(v, dict):
      print_dict(v, step+1)
    if isinstance(v, list):
      print_list(v,step+1)
    else:
      if isinstance(v,unicode):
        v = v.encode('utf-8')
      print ">>"*step, v

def print_list (llist, step=1):
  """
  print list data
  """
  for it in llist:
    if isinstance(it, dict):
      print_dict(it, step+1)
    elif isinstance(it,list):
      print_list(it, step+1)
    else:
      if isinstance(it,unicode):
        it = it.encode('utf-8')
      print "++"*step, it

def parse_wiki_data_dict(wdict,title):
  """
  parsing wiki data json
  """
  wiki_page_ret_list = []
  for key in KEY_LIST:
    for cn in CN_LIST:
      try:
        data = wdict[key][cn]['value'].encode('utf-8')
        wiki_page_ret_list.append([title, key, cn, data])
      except Exception, e:
        continue

  for wiki in WIKI_LIST:
    try:
      data = wdict['sitelinks'][wiki]['title'].encode('utf-8')
      wiki_page_ret_list.append([title, "wiki", wiki, data])
    except:
      continue
  return wiki_page_ret_list

def processing_wiki_page(wpage):
  """
  page parsing
  """
  h = HTMLParser.HTMLParser()
  #print wpage[0:3], len(wpage)
  title = ''
  if wpage[1].startswith("<title>"):
    title = wpage[1].replace("<title>","").replace("</title>","")
  if title.startswith("Q"):
    print >> sys.stderr, "Do process page ", title
    for item in wpage:
      if item.startswith("<text xml:space=\"preserve\">"):
        item = item[27:]
        item = item.replace("</text>","")
        item = h.unescape(item)
        data = json.loads(item) 
        #print item
        #print data.keys()
        page_results = parse_wiki_data_dict(data,title)
        if len(page_results)>0:
          for ret in page_results:
            print "\t".join(ret)
  else:
    return None

########
# main #
########
def main(fin, fout):
  """
  extracting wiki data program
  @param  fin   input file
  @param  fout  output file
  """
  h = HTMLParser.HTMLParser()
  wiki_page = []
  page_flag = 0

  for line in fin:
    line = line.strip()
    if line=="<page>":
      if page_flag == 0:
        page_flag=1
      if page_flag == 1 and len(wiki_page)>0:
        processing_wiki_page(wiki_page)
        wiki_page =[]
      wiki_page.append(line)
      continue
    if page_flag==1:
      wiki_page.append(line)
  if len(wiki_page)>0:
    processing_wiki_page(wiki_page)

if __name__ == '__main__':
  _PARSER = argparse.ArgumentParser(description='cat program')
  _PARSER.add_argument('--input', help='input file <default: stdin>', metavar='FILE', type=file, default=sys.stdin)
  _PARSER.add_argument('--output', help='output file <default: stdout>', metavar='FILE',
      type=argparse.FileType('w'), default=sys.stdout)
  _PARSER.add_argument('--log-level', help='set logging level', metavar='LEVEL')
  _PARSER.add_argument('--log-file', help='set log file <default: stderr>', metavar='FILE')
  _ARGS = _PARSER.parse_args()
  _LOG_CFG = {'format':'[%(asctime)-15s] %(levelname)-8s %(message)s', 'datefmt':'%Y-%m-%d %H:%M:%S'}
  if _ARGS.log_level:
    _LOG_CFG['level'] = eval('logging.%s' % _ARGS.log_level.upper())
  if _ARGS.log_file:
    _LOG_CFG['filename'] = _ARGS.log_file
  logging.basicConfig(**_LOG_CFG)    # pylint: disable=W0142
  main(_ARGS.input, _ARGS.output)
