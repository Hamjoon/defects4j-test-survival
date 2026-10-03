# Part 2 handover A — Step 3 stop

Steps 1–3 are complete. Stop here for Gary/Cowork review of the real developer populations and the round policy. No Step 4 generation, no new API calls, and no push.

## Baseline and round-policy input

| Record / CUT | Dev classes | Missing | Compiled | Dev methods listed | D_r | Fail/error at t | Trigger fail/error | Timeouts | L_r(1) | Target reached |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 4 / LookupTranslator | 4 | 0 | 4 | 137 | 136 | 1 | 1/1 | 0 | 53 | no |
| 5 / LocaleUtils | 1 | 0 | 1 | 13 | 12 | 1 | 1/1 | 0 | 130 | yes |
| 6 / CharSequenceTranslator | 9 | 0 | 9 | 142 | 141 | 1 | 1/1 | 0 | 57 | no |
| 11 / RandomStringUtils | 1 | 0 | 1 | 11 | 10 | 1 | 1/1 | 0 | 104 | yes |
| 12 / RandomStringUtils | 1 | 0 | 1 | 10 | 8 | 2 | 2/2 | 0 | 87 | yes |
| 13 / SerializationUtils | 12 | 0 | 12 | 208 | 207 | 1 | 1/1 | 0 | 43 | no |
| 17 / CharSequenceTranslator | 8 | 0 | 8 | 45 | 44 | 1 | 1/1 | 0 | 49 | yes |
| 19 / NumericEntityUnescaper | 3 | 0 | 3 | 32 | 30 | 2 | 2/2 | 0 | 53 | yes |
| 28 / NumericEntityUnescaper | 2 | 0 | 2 | 20 | 19 | 1 | 1/1 | 0 | 61 | yes |
| 43 / ExtendedMessageFormat | 1 | 0 | 1 | 7 | 6 | 1 | 1/1 | 0 | 38 | yes |
| 54 / LocaleUtils | 1 | 0 | 1 | 12 | 11 | 1 | 1/1 | 0 | 76 | yes |
| 55 / StopWatch | 1 | 0 | 1 | 6 | 5 | 1 | 1/1 | 0 | 66 | yes |
| 57 / LocaleUtils | 1 | 0 | 1 | 11 | 0 | 11 | 11/11 | 0 | 139 | yes |
| 64 / ValuedEnum | 4 | 0 | 4 | 75 | 74 | 1 | 1/1 | 0 | 30 | no |

Total passing populations across records: developer 703; round-1 LLM 986. 10/14 records already meet the target. Counts are record-specific; these totals do not deduplicate shared test methods across records.

All 49 developer test classes compile. Of 68 structured LLM files, 59 compile and 9 fail compilation. The compiled LLM files list 1085 methods: 986 pass, 71 assertion failures, 25 other errors, and 3 timeouts. Every listed method has a result; none is not-run.

Default policy pending review: five calls per additional round (one per technique), stop each record at L_r(k) ≥ D_r or 30 total rounds. Existing round 1 is always reused.

## Extraction comparison

### Part 2 round-1 extraction

| Technique | Responses | MSR | Bundle CSR | CSR v2 |
|---|---:|---:|---:|---:|
| ZSL | 14 | 14 | 5 | 13 |
| FSL | 14 | 14 | 5 | 14 |
| CoT | 14 | 14 | 5 | 13 |
| ToT | 14 | 14 | 4 | 14 |
| GToT | 14 | 14 | 6 | 14 |
| pooled | 70 | 70 | 25 | 68 |

Source bytes between the selected marker lines (or fallback fences) are retained; only lines starting with ``` are removed. No stripping, formatting or test repair.


Both excluded responses ended with finish_reason=length in Part 1. Lang-12 ZSL has no complete marker pair or closed fenced block; Lang-54 CoT falls back to a closed snippet without a class. MSR records visible code even when a truncated response has no extractable complete block.

## Runner verification

```json
{
  "extraction_checks": "passed",
  "runs": {
    "RunnerFixture": {
      "counts": {
        "pass": 2,
        "fail": 1,
        "error": 1,
        "ignored": 2,
        "timeout": 1
      },
      "listed": 7,
      "launches": 2
    },
    "CrashFixture": {
      "counts": {
        "pass": 1,
        "not-run": 2
      },
      "listed": 3,
      "launches": 1
    },
    "LegacyFixture": {
      "counts": {
        "fail": 1,
        "pass": 1
      },
      "listed": 2,
      "launches": 1
    },
    "Lang-4-ZSL": {
      "counts": {
        "fail": 1,
        "pass": 9
      },
      "listed": 10,
      "launches": 1
    },
    "Lang-11-ZSL": {
      "counts": {
        "pass": 14,
        "timeout": 1
      },
      "listed": 15,
      "launches": 2
    }
  }
}
```

The Lang-4 ZSL control retained 9 passes and 1 assertion failure. Lang-11 ZSL lists all 15 methods, reports exactly 1 timeout at 30 seconds and measures the other 14 as passes. The wrapper excludes all already measured methods on relaunch, so successful methods are not repeated. Synthetic fixtures verify failure/error/ignored classification, JUnit 3, timeout resumption and crash not-run accounting.

## Developer and LLM detail

| Record | Structured files | Compiled files | Listed methods | Pass | Fail | Error | Ignored | Timeout | Not-run |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 5 | 5 | 57 | 53 | 4 | 0 | 0 | 0 | 0 |
| 5 | 5 | 5 | 139 | 130 | 9 | 0 | 0 | 0 | 0 |
| 6 | 5 | 4 | 62 | 57 | 3 | 2 | 0 | 0 | 0 |
| 11 | 5 | 5 | 108 | 104 | 1 | 1 | 0 | 2 | 0 |
| 12 | 4 | 4 | 96 | 87 | 0 | 8 | 0 | 1 | 0 |
| 13 | 5 | 3 | 46 | 43 | 1 | 2 | 0 | 0 | 0 |
| 17 | 5 | 5 | 65 | 49 | 16 | 0 | 0 | 0 | 0 |
| 19 | 5 | 5 | 61 | 53 | 7 | 1 | 0 | 0 | 0 |
| 28 | 5 | 5 | 66 | 61 | 4 | 1 | 0 | 0 | 0 |
| 43 | 5 | 3 | 53 | 38 | 8 | 7 | 0 | 0 | 0 |
| 54 | 4 | 3 | 80 | 76 | 4 | 0 | 0 | 0 | 0 |
| 55 | 5 | 4 | 75 | 66 | 9 | 0 | 0 | 0 | 0 |
| 57 | 5 | 5 | 145 | 139 | 3 | 3 | 0 | 0 | 0 |
| 64 | 5 | 3 | 32 | 30 | 2 | 0 | 0 | 0 | 0 |

### Trigger methods

| Bug | Trigger method | Status at t |
|---|---|---|
| 4 | `org.apache.commons.lang3.text.translate.LookupTranslatorTest::testLang882` | fail |
| 5 | `org.apache.commons.lang3.LocaleUtilsTest::testLang865` | error |
| 6 | `org.apache.commons.lang3.StringUtilsTest::testEscapeSurrogatePairs` | error |
| 11 | `org.apache.commons.lang3.RandomStringUtilsTest::testLANG807` | fail |
| 12 | `org.apache.commons.lang3.RandomStringUtilsTest::testExceptions` | error |
| 12 | `org.apache.commons.lang3.RandomStringUtilsTest::testLANG805` | error |
| 13 | `org.apache.commons.lang3.SerializationUtilsTest::testPrimitiveTypeClassSerialization` | error |
| 17 | `org.apache.commons.lang3.StringEscapeUtilsTest::testLang720` | fail |
| 19 | `org.apache.commons.lang3.text.translate.NumericEntityUnescaperTest::testUnfinishedEntity` | error |
| 19 | `org.apache.commons.lang3.text.translate.NumericEntityUnescaperTest::testOutOfBounds` | error |
| 28 | `org.apache.commons.lang3.text.translate.NumericEntityUnescaperTest::testSupplementaryUnescaping` | fail |
| 43 | `org.apache.commons.lang.text.ExtendedMessageFormatTest::testEscapedQuote_LANG_477` | error |
| 54 | `org.apache.commons.lang.LocaleUtilsTest::testLang328` | error |
| 55 | `org.apache.commons.lang.time.StopWatchTest::testLang315` | fail |
| 57 | `org.apache.commons.lang.LocaleUtilsTest::testAvailableLocaleSet` | error |
| 57 | `org.apache.commons.lang.LocaleUtilsTest::testIsAvailableLocale` | error |
| 57 | `org.apache.commons.lang.LocaleUtilsTest::testAvailableLocaleList` | error |
| 57 | `org.apache.commons.lang.LocaleUtilsTest::testCountriesByLanguage` | error |
| 57 | `org.apache.commons.lang.LocaleUtilsTest::testLocaleLookupList_LocaleLocale` | error |
| 57 | `org.apache.commons.lang.LocaleUtilsTest::testLanguagesByCountry` | error |
| 57 | `org.apache.commons.lang.LocaleUtilsTest::testToLocale_1Part` | error |
| 57 | `org.apache.commons.lang.LocaleUtilsTest::testToLocale_2Part` | error |
| 57 | `org.apache.commons.lang.LocaleUtilsTest::testToLocale_3Part` | error |
| 57 | `org.apache.commons.lang.LocaleUtilsTest::testLocaleLookupList_Locale` | error |
| 57 | `org.apache.commons.lang.LocaleUtilsTest::testConstructor` | error |
| 64 | `org.apache.commons.lang.enums.ValuedEnumTest::testCompareTo_otherEnumType` | fail |

Developer statuses: {'pass': 703, 'fail': 6, 'error': 20}. LLM statuses: {'fail': 71, 'pass': 986, 'error': 25, 'timeout': 3}.

The 26 developer fail/error results are exactly the 26 declared trigger methods. Classpath precedence is copied/generated classes, tools/runner, checkout cp.test, then pinned JUnit/Hamcrest. The project JUnit in cp.test retains its prescribed precedence.

## Timeline

### Part 2 timeline

Order of buggy revisions: Lang-64b → Lang-57b → Lang-55b → Lang-54b → Lang-43b → Lang-28b → Lang-19b → Lang-17b → Lang-13b → Lang-12b → Lang-11b → Lang-6b → Lang-5b → Lang-4b

Presence uses the original package path. Days are exact elapsed days rounded to six decimals here; JSON retains nine decimals and calendar-day gaps. The own fixed version is always step 1.

| Record | Step | Time point | Revision date | Days after t | CUT |
|---|---:|---|---|---:|---|
| Lang-4 / LookupTranslator | 1 | Lang-4f | 2013-04-23 06:00:41 +0000 | 1.071030 | present |
| Lang-5 / LocaleUtils | 1 | Lang-5f | 2013-01-03 06:19:52 +0000 | 16.743519 | present |
| Lang-5 / LocaleUtils | 2 | Lang-4b | 2013-04-22 04:18:24 +0000 | 125.659167 | present |
| Lang-6 / CharSequenceTranslator | 1 | Lang-6f | 2012-11-20 20:45:50 +0000 | 7.308484 | present |
| Lang-6 / CharSequenceTranslator | 2 | Lang-5b | 2012-12-17 12:29:12 +0000 | 33.963600 | present |
| Lang-6 / CharSequenceTranslator | 3 | Lang-4b | 2013-04-22 04:18:24 +0000 | 159.622766 | present |
| Lang-11 / RandomStringUtils | 1 | Lang-11f | 2012-06-10 12:40:48 +0000 | 0.904329 | present |
| Lang-11 / RandomStringUtils | 2 | Lang-6b | 2012-11-13 13:21:37 +0000 | 156.932674 | present |
| Lang-11 / RandomStringUtils | 3 | Lang-5b | 2012-12-17 12:29:12 +0000 | 190.896273 | present |
| Lang-11 / RandomStringUtils | 4 | Lang-4b | 2013-04-22 04:18:24 +0000 | 316.555440 | present |
| Lang-12 / RandomStringUtils | 1 | Lang-12f | 2012-06-09 14:58:34 +0000 | 0.012211 | present |
| Lang-12 / RandomStringUtils | 2 | Lang-11b | 2012-06-09 14:58:34 +0000 | 0.012211 | present |
| Lang-12 / RandomStringUtils | 3 | Lang-6b | 2012-11-13 13:21:37 +0000 | 156.944884 | present |
| Lang-12 / RandomStringUtils | 4 | Lang-5b | 2012-12-17 12:29:12 +0000 | 190.908484 | present |
| Lang-12 / RandomStringUtils | 5 | Lang-4b | 2013-04-22 04:18:24 +0000 | 316.567650 | present |
| Lang-13 / SerializationUtils | 1 | Lang-13f | 2012-02-29 14:39:01 +0000 | 0.009780 | present |
| Lang-13 / SerializationUtils | 2 | Lang-12b | 2012-06-09 14:40:59 +0000 | 101.011146 | present |
| Lang-13 / SerializationUtils | 3 | Lang-11b | 2012-06-09 14:58:34 +0000 | 101.023356 | present |
| Lang-13 / SerializationUtils | 4 | Lang-6b | 2012-11-13 13:21:37 +0000 | 257.956030 | present |
| Lang-13 / SerializationUtils | 5 | Lang-5b | 2012-12-17 12:29:12 +0000 | 291.919630 | present |
| Lang-13 / SerializationUtils | 6 | Lang-4b | 2013-04-22 04:18:24 +0000 | 417.578796 | present |
| Lang-17 / CharSequenceTranslator | 1 | Lang-17f | 2011-07-14 18:49:51 +0000 | 0.587917 | present |
| Lang-17 / CharSequenceTranslator | 2 | Lang-13b | 2012-02-29 14:24:56 +0000 | 230.403947 | present |
| Lang-17 / CharSequenceTranslator | 3 | Lang-12b | 2012-06-09 14:40:59 +0000 | 331.415093 | present |
| Lang-17 / CharSequenceTranslator | 4 | Lang-11b | 2012-06-09 14:58:34 +0000 | 331.427303 | present |
| Lang-17 / CharSequenceTranslator | 5 | Lang-6b | 2012-11-13 13:21:37 +0000 | 488.359977 | present |
| Lang-17 / CharSequenceTranslator | 6 | Lang-5b | 2012-12-17 12:29:12 +0000 | 522.323576 | present |
| Lang-17 / CharSequenceTranslator | 7 | Lang-4b | 2013-04-22 04:18:24 +0000 | 647.982743 | present |
| Lang-19 / NumericEntityUnescaper | 1 | Lang-19f | 2011-07-03 07:55:33 +0000 | 0.033345 | present |
| Lang-19 / NumericEntityUnescaper | 2 | Lang-17b | 2011-07-14 04:43:15 +0000 | 10.899803 | present |
| Lang-19 / NumericEntityUnescaper | 3 | Lang-13b | 2012-02-29 14:24:56 +0000 | 241.303750 | present |
| Lang-19 / NumericEntityUnescaper | 4 | Lang-12b | 2012-06-09 14:40:59 +0000 | 342.314896 | present |
| Lang-19 / NumericEntityUnescaper | 5 | Lang-11b | 2012-06-09 14:58:34 +0000 | 342.327106 | present |
| Lang-19 / NumericEntityUnescaper | 6 | Lang-6b | 2012-11-13 13:21:37 +0000 | 499.259780 | present |
| Lang-19 / NumericEntityUnescaper | 7 | Lang-5b | 2012-12-17 12:29:12 +0000 | 533.223380 | present |
| Lang-19 / NumericEntityUnescaper | 8 | Lang-4b | 2013-04-22 04:18:24 +0000 | 658.882546 | present |
| Lang-28 / NumericEntityUnescaper | 1 | Lang-28f | 2010-06-22 06:34:18 +0000 | 0.010289 | present |
| Lang-28 / NumericEntityUnescaper | 2 | Lang-19b | 2011-07-03 07:07:32 +0000 | 376.033368 | present |
| Lang-28 / NumericEntityUnescaper | 3 | Lang-17b | 2011-07-14 04:43:15 +0000 | 386.933171 | present |
| Lang-28 / NumericEntityUnescaper | 4 | Lang-13b | 2012-02-29 14:24:56 +0000 | 617.337118 | present |
| Lang-28 / NumericEntityUnescaper | 5 | Lang-12b | 2012-06-09 14:40:59 +0000 | 718.348264 | present |
| Lang-28 / NumericEntityUnescaper | 6 | Lang-11b | 2012-06-09 14:58:34 +0000 | 718.360475 | present |
| Lang-28 / NumericEntityUnescaper | 7 | Lang-6b | 2012-11-13 13:21:37 +0000 | 875.293148 | present |
| Lang-28 / NumericEntityUnescaper | 8 | Lang-5b | 2012-12-17 12:29:12 +0000 | 909.256748 | present |
| Lang-28 / NumericEntityUnescaper | 9 | Lang-4b | 2013-04-22 04:18:24 +0000 | 1034.915914 | present |
| Lang-43 / ExtendedMessageFormat | 1 | Lang-43f | 2009-01-09 22:05:14 +0000 | 35.229722 | present |
| Lang-43 / ExtendedMessageFormat | 2 | Lang-28b | 2010-06-22 06:19:29 +0000 | 563.572951 | absent |
| Lang-43 / ExtendedMessageFormat | 3 | Lang-19b | 2011-07-03 07:07:32 +0000 | 939.606319 | absent |
| Lang-43 / ExtendedMessageFormat | 4 | Lang-17b | 2011-07-14 04:43:15 +0000 | 950.506123 | absent |
| Lang-43 / ExtendedMessageFormat | 5 | Lang-13b | 2012-02-29 14:24:56 +0000 | 1180.910069 | absent |
| Lang-43 / ExtendedMessageFormat | 6 | Lang-12b | 2012-06-09 14:40:59 +0000 | 1281.921215 | absent |
| Lang-43 / ExtendedMessageFormat | 7 | Lang-11b | 2012-06-09 14:58:34 +0000 | 1281.933426 | absent |
| Lang-43 / ExtendedMessageFormat | 8 | Lang-6b | 2012-11-13 13:21:37 +0000 | 1438.866100 | absent |
| Lang-43 / ExtendedMessageFormat | 9 | Lang-5b | 2012-12-17 12:29:12 +0000 | 1472.829699 | absent |
| Lang-43 / ExtendedMessageFormat | 10 | Lang-4b | 2013-04-22 04:18:24 +0000 | 1598.488866 | absent |
| Lang-54 / LocaleUtils | 1 | Lang-54f | 2007-05-01 23:50:01 +0000 | 11.776563 | present |
| Lang-54 / LocaleUtils | 2 | Lang-43b | 2008-12-05 16:34:26 +0000 | 595.474074 | present |
| Lang-54 / LocaleUtils | 3 | Lang-28b | 2010-06-22 06:19:29 +0000 | 1159.047025 | absent |
| Lang-54 / LocaleUtils | 4 | Lang-19b | 2011-07-03 07:07:32 +0000 | 1535.080394 | absent |
| Lang-54 / LocaleUtils | 5 | Lang-17b | 2011-07-14 04:43:15 +0000 | 1545.980197 | absent |
| Lang-54 / LocaleUtils | 6 | Lang-13b | 2012-02-29 14:24:56 +0000 | 1776.384144 | absent |
| Lang-54 / LocaleUtils | 7 | Lang-12b | 2012-06-09 14:40:59 +0000 | 1877.395289 | absent |
| Lang-54 / LocaleUtils | 8 | Lang-11b | 2012-06-09 14:58:34 +0000 | 1877.407500 | absent |
| Lang-54 / LocaleUtils | 9 | Lang-6b | 2012-11-13 13:21:37 +0000 | 2034.340174 | absent |
| Lang-54 / LocaleUtils | 10 | Lang-5b | 2012-12-17 12:29:12 +0000 | 2068.303773 | absent |
| Lang-54 / LocaleUtils | 11 | Lang-4b | 2013-04-22 04:18:24 +0000 | 2193.962940 | absent |
| Lang-55 / StopWatch | 1 | Lang-55f | 2007-02-06 22:49:50 +0000 | 0.003669 | present |
| Lang-55 / StopWatch | 2 | Lang-54b | 2007-04-20 05:11:46 +0000 | 72.268900 | present |
| Lang-55 / StopWatch | 3 | Lang-43b | 2008-12-05 16:34:26 +0000 | 667.742975 | present |
| Lang-55 / StopWatch | 4 | Lang-28b | 2010-06-22 06:19:29 +0000 | 1231.315926 | absent |
| Lang-55 / StopWatch | 5 | Lang-19b | 2011-07-03 07:07:32 +0000 | 1607.349294 | absent |
| Lang-55 / StopWatch | 6 | Lang-17b | 2011-07-14 04:43:15 +0000 | 1618.249097 | absent |
| Lang-55 / StopWatch | 7 | Lang-13b | 2012-02-29 14:24:56 +0000 | 1848.653044 | absent |
| Lang-55 / StopWatch | 8 | Lang-12b | 2012-06-09 14:40:59 +0000 | 1949.664190 | absent |
| Lang-55 / StopWatch | 9 | Lang-11b | 2012-06-09 14:58:34 +0000 | 1949.676400 | absent |
| Lang-55 / StopWatch | 10 | Lang-6b | 2012-11-13 13:21:37 +0000 | 2106.609074 | absent |
| Lang-55 / StopWatch | 11 | Lang-5b | 2012-12-17 12:29:12 +0000 | 2140.572674 | absent |
| Lang-55 / StopWatch | 12 | Lang-4b | 2013-04-22 04:18:24 +0000 | 2266.231840 | absent |
| Lang-57 / LocaleUtils | 1 | Lang-57f | 2006-12-22 20:34:37 +0000 | 0.030069 | present |
| Lang-57 / LocaleUtils | 2 | Lang-55b | 2007-02-06 22:44:33 +0000 | 46.120301 | present |
| Lang-57 / LocaleUtils | 3 | Lang-54b | 2007-04-20 05:11:46 +0000 | 118.389201 | present |
| Lang-57 / LocaleUtils | 4 | Lang-43b | 2008-12-05 16:34:26 +0000 | 713.863275 | present |
| Lang-57 / LocaleUtils | 5 | Lang-28b | 2010-06-22 06:19:29 +0000 | 1277.436227 | absent |
| Lang-57 / LocaleUtils | 6 | Lang-19b | 2011-07-03 07:07:32 +0000 | 1653.469595 | absent |
| Lang-57 / LocaleUtils | 7 | Lang-17b | 2011-07-14 04:43:15 +0000 | 1664.369398 | absent |
| Lang-57 / LocaleUtils | 8 | Lang-13b | 2012-02-29 14:24:56 +0000 | 1894.773345 | absent |
| Lang-57 / LocaleUtils | 9 | Lang-12b | 2012-06-09 14:40:59 +0000 | 1995.784491 | absent |
| Lang-57 / LocaleUtils | 10 | Lang-11b | 2012-06-09 14:58:34 +0000 | 1995.796701 | absent |
| Lang-57 / LocaleUtils | 11 | Lang-6b | 2012-11-13 13:21:37 +0000 | 2152.729375 | absent |
| Lang-57 / LocaleUtils | 12 | Lang-5b | 2012-12-17 12:29:12 +0000 | 2186.692975 | absent |
| Lang-57 / LocaleUtils | 13 | Lang-4b | 2013-04-22 04:18:24 +0000 | 2312.352141 | absent |
| Lang-64 / ValuedEnum | 1 | Lang-64f | 2006-08-18 22:21:47 +0000 | 0.104410 | present |
| Lang-64 / ValuedEnum | 2 | Lang-57b | 2006-12-22 19:51:19 +0000 | 125.999919 | present |
| Lang-64 / ValuedEnum | 3 | Lang-55b | 2007-02-06 22:44:33 +0000 | 172.120220 | present |
| Lang-64 / ValuedEnum | 4 | Lang-54b | 2007-04-20 05:11:46 +0000 | 244.389120 | present |
| Lang-64 / ValuedEnum | 5 | Lang-43b | 2008-12-05 16:34:26 +0000 | 839.863194 | present |
| Lang-64 / ValuedEnum | 6 | Lang-28b | 2010-06-22 06:19:29 +0000 | 1403.436146 | absent |
| Lang-64 / ValuedEnum | 7 | Lang-19b | 2011-07-03 07:07:32 +0000 | 1779.469514 | absent |
| Lang-64 / ValuedEnum | 8 | Lang-17b | 2011-07-14 04:43:15 +0000 | 1790.369317 | absent |
| Lang-64 / ValuedEnum | 9 | Lang-13b | 2012-02-29 14:24:56 +0000 | 2020.773264 | absent |
| Lang-64 / ValuedEnum | 10 | Lang-12b | 2012-06-09 14:40:59 +0000 | 2121.784410 | absent |
| Lang-64 / ValuedEnum | 11 | Lang-11b | 2012-06-09 14:58:34 +0000 | 2121.796620 | absent |
| Lang-64 / ValuedEnum | 12 | Lang-6b | 2012-11-13 13:21:37 +0000 | 2278.729294 | absent |
| Lang-64 / ValuedEnum | 13 | Lang-5b | 2012-12-17 12:29:12 +0000 | 2312.692894 | absent |
| Lang-64 / ValuedEnum | 14 | Lang-4b | 2013-04-22 04:18:24 +0000 | 2438.352060 | absent |

#### Package boundary

- Lang-43 (org.apache.commons.lang.text.ExtendedMessageFormat): first absent at Lang-28b.
- Lang-54 (org.apache.commons.lang.LocaleUtils): first absent at Lang-28b.
- Lang-55 (org.apache.commons.lang.time.StopWatch): first absent at Lang-28b.
- Lang-57 (org.apache.commons.lang.LocaleUtils): first absent at Lang-28b.
- Lang-64 (org.apache.commons.lang.enums.ValuedEnum): first absent at Lang-28b.

#### No later dataset bug

- Lang-4b: own fixed version remains available as step 1; no chronologically later dataset buggy revision.


All 28 checkouts compiled. The five Lang 2.x records lose their original package paths at the first sampled Lang 3.x point. The latest buggy record has its own fixed point and no later dataset buggy point.

## Anomalies and implementation notes

- Lang-6 ZSL: compile failure, {'other': 2}; `generated/p2/Lang-6/r1/ZSL/javac.err`.
- Lang-13 FSL: compile failure, {'CFS': 4}; `generated/p2/Lang-13/r1/FSL/javac.err`.
- Lang-13 CoT: compile failure, {'CFS': 1}; `generated/p2/Lang-13/r1/CoT/javac.err`.
- Lang-43 FSL: compile failure, {'CFS': 24}; `generated/p2/Lang-43/r1/FSL/javac.err`.
- Lang-43 GToT: compile failure, {'AR': 1}; `generated/p2/Lang-43/r1/GToT/javac.err`.
- Lang-54 ToT: compile failure, {'IT': 2}; `generated/p2/Lang-54/r1/ToT/javac.err`.
- Lang-55 ZSL: compile failure, {'CFS': 2}; `generated/p2/Lang-55/r1/ZSL/javac.err`.
- Lang-64 ZSL: compile failure, {'other': 1}; `generated/p2/Lang-64/r1/ZSL/javac.err`.
- Lang-64 CoT: compile failure, {'PDNE': 10, 'CFS': 10}; `generated/p2/Lang-64/r1/CoT/javac.err`.
- llm Lang-11 ZSL `org.apache.commons.lang3.RandomStringUtilsTest::testPrivateHighSurrogateIsSkipped`: timeout, launch 1.
- llm Lang-11 GToT `org.apache.commons.lang3.RandomStringUtilsTest::testRandom_privateHighSurrogateIsSkipped`: timeout, launch 1.
- llm Lang-12 CoT `org.apache.commons.lang3.RandomStringUtilsTest::testRandomWithSurrogateRangeDoesNotThrow`: timeout, launch 1.
- Lang-57: D_r = 0. All 11 declared trigger methods fail/error in shared setup; there is no passing developer population for this record. The default count target is already met at zero.

- No generated or developer test source was repaired, reformatted, or normalized. SHA-256 and byte equality verify provenance.
- File compilation failures are retained and excluded at t; source syntax is not an additional filter after CSR v2.
- Initial developer execution from /work caused two FileNotFoundExceptions in testLang708 (Lang-4 and Lang-6). The initial baseline and every per-class log are preserved under results/archive/part2-initial-cwd/. The complete developer baseline was repeated with each checkout as working directory and absolute classpaths; LLM baseline execution uses the same convention. No test/resource files or model output were edited. Per-method status changes are recorded in results/p2-cwd-correction.json: [{"bug_id": 4, "fqcn": "org.apache.commons.lang3.StringEscapeUtilsTest", "method": "testLang708", "before": "error", "after": "pass"}, {"bug_id": 6, "fqcn": "org.apache.commons.lang3.StringEscapeUtilsTest", "method": "testLang708", "before": "error", "after": "pass"}].
- The runtime uses Request.method in a fresh worker per method. Each method receives its own fixtures; static JVM state persists within a launch, and timeout recovery necessarily starts a new JVM.
- Fixed versions remain step 1; actual revision-date gaps are retained rather than silently setting them to zero. A later day-bin aggregation can label the fixed step as bin 0 while preserving these source dates.
- Mechanical setup corrections: an initial combined patch was rejected atomically for targeting the runner twice; it was reapplied as separate file writes. An initial smoke-script write used the docker subdirectory as cwd and created no file; the path was corrected. Docker socket access was blocked in the sandbox and was rerun with escalation. Exploratory reads of guessed filenames were corrected after inspecting the actual repository layout.

## Recorded workload times and cost

- Step 2 checkouts, compiles, exports and timeline: 198.073 seconds.
- Step 3 developer baseline: 62.681 seconds; LLM baseline: 128.013 seconds.
- Archived initial developer baseline before cwd correction: 67.067 seconds.
- Step 1 per-run timing is saved in results/p2-smoke/*.summary.json; full editing/session wall time was not reconstructed.
- Part 2 API calls and cost through this handover: 0 calls / $0. Round 1 reuses the 70 existing Part 1 responses.

## Verification

See results/p2-validation.json for immutable-source checks, method-count reconciliation, timeline ordering/presence, classpath precedence, and credential scanning.

Code/document whitespace checks pass. Unrestricted git diff --check reports retained CSV CRLF/source whitespace; immutable source and evidence were not normalized to suppress these diagnostics.

## Open review decision

Approve or revise the generation-round policy using D_r and L_r(1) above before Step 4. The default remains five techniques per round with a maximum of 30 total rounds per record.

Lang-57 has D_r = 0 because all developer methods trigger the bug in setup. Its developer survival percentage has a zero denominator; the later report should show N/A. Review how this record should enter the class-level 2×2 analysis before those later stages.
