# extractor-wiki-data

## dump wiki-data

```
wget http://dumps.wikimedia.org/wikidatawiki/latest/wikidatawiki-latest-pages-articles.xml.bz2
```

## run script

```
$ bzip2 -dc ./wikidatawiki-latest-pages-articles.xml.bz2 | python ./extractor-wiki-data.py  2> /dev/null  | head -n 30
Q15     labels  en      Africa
Q15     labels  ja      アフリカ
Q15     labels  zh      非洲
Q15     labels  ko      아프리카
Q15     labels  fr      Afrique
Q15     labels  ar      أفريقيا
Q15     labels  de      Afrika
Q15     labels  es      África
Q15     labels  tr      Afrika
Q15     labels  vi      châu Phi
Q15     labels  pt      África
Q15     labels  ru      Африка
Q15     descriptions    en      continent
Q15     descriptions    ja      大陸
Q15     descriptions    zh      七大洲之一
Q15     descriptions    ko      아시아 다음으로 면적이 넓고 인구가 많은 대륙
Q15     descriptions    fr      continent
Q15     descriptions    ar      قارة
Q15     descriptions    de      Kontinent
Q15     descriptions    es      continente
Q15     descriptions    pt      continente
Q15     descriptions    ru      второй по площади континент после Евразии,омываемый Средиземным морем с севера
Q15     wiki    enwiki  Africa
Q15     wiki    jawiki  アフリカ
Q15     wiki    zhwiki  非洲
Q15     wiki    kowiki  아프리카
Q15     wiki    frwiki  Afrique
Q15     wiki    arwiki  أفريقيا
Q15     wiki    dewiki  Afrika
Q15     wiki    eswiki  África
...
```

