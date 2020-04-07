# Washington 2018 General Election Shapefile

This shapefile combines election results with precinct geometries for the 2018 Washington State General Election.

## Sources
For the shapefile I am using the file named "2018Precincts_VERIFIED.zip" at [this link.](https://www.sos.wa.gov/elections/research/precinct-shapefiles.aspx)

Election results come from the [MIT Election Data Science Lab](https://github.com/MEDSL/2018-elections-official/blob/master/precinct_2018.zip).

Source files and addiontal supporting documentation can also be found in [this repository.](https://github.com/OpenPrecincts/WA18G)

## Metadata

* `loc_prec`: Unique precinct identifier, locality and precinct separated by a comma (locality = county in Washington).
* `county`: County name
* `countyFips`: County FIPS code
* `precinct`: Precinct code
* `prec_name`: Precinct name
* `FullPrc`: Unique identifier for rows in the source shapefile
* `G18DSEN`: General 2018 U.S. Senate Democratic Party Candidate
* `G18RSEN`: General 2018 U.S. Senate Republican Party Candidate
* `G18NPSEN`:   General 2018 U.S. Sentate No Party Preference Candidate
* `G18DHOR`: General 2018 U.S. House Democratic Party Candidate
* `G18RHOR`: General 2018 U.S. House Republican Party Candidate
* `G18LHOR`:    General 2018 U.S. House Libertarian Party Candidate
* `G18NPHOR`:   General 2018 U.S. House No Party Preference Candidate
* `G18DStHou1`: General 2018 State House Democratic Party Candidate Position 1
* `G18DStHou2`: General 2018 State House Democratic Party Candidate Position 2
* `G18DStSen`:  General 2018 State Senate Democratic Party Candidate
* `G18RStHou1`: General 2018 State House Republican Party Candidate Position 1
* `G18RStHou2`: General 2018 State House Republican Party Candidate Position 2 
* `G18RStSen`:  General 2018 State Senate Republican Party Candidate
* `G18IStHou1`: General 2018 State House Independent Party Candidate Position 1
* `G18IStHou2`: General 2018 State House Independent Party Candidate Position 2
* `G18IStSen`:  General 2018 State Senate Independent Party Candidate
* `G18LStHou1`: General 2018 State House Libertarian Party Candidate Position 1
* `G18LStHou2`: General 2018 State House Libertarian Party Candidate Position 2
* `G18LStSen`:  General 2018 State Senate Libertarian Party Candidate
* `G18NPStHo1`: General 2018 State House No Party Preference Candidate Position 1
* `G18NPStHo2`: General 2018 State House No Party Preference Candidate Position 2
* `G18NPStSen`: General 2018 State Sentate No Party Preference Candidate

## Processing

The MIT election results dataset is processed to be sorted by precinct and aggregated by party and office per precinct. Then, the string manipulations in [`match_election_result_to_geometry.py`](https://github.com/OpenPrecincts/WA18G) were applied to find common precinct names between the election results and shapefile. Next, the two files were merged on those common names resulting a succesful matching with a few exception that will be detailed below:

### Precinct Geometries Missing Election Results

[Breakdown by County](https://github.com/OpenPrecincts/WA18G/tree/master/geometries_missing_results_by_county)

All reasons listed in the tables below described why the precinct shapes in the [source shapefile](https://www.sos.wa.gov/elections/research/precinct-shapefiles.aspx) had no corresponding eleciton results. The reasons were verified with the approriate county board of elections.

- Precincts with no voters were zero filled for all election contests
- Precinct geometries that were combined with another precinct by the county were [dissolved](https://grindgis.com/software/qgis/basic-editing-tools-in-qgis) into the precinct to which their votes were allocated. 


[Benton](https://github.com/OpenPrecincts/WA18G/tree/master/geometries_missing_results_by_county/Benton%20County)
|CountyCd|PrcCode|FullPrc   |prec_name  |population estimate|reason|
|--------|-------|----------|-----------|----------|----------|
|BE      |1291   |BE00001291|Ida        |5         | No voters
|BE      |1292   |BE00001292|Ridge      |2         | No voters
|BE      |1364   |BE00001364|Wheat      |0         | No voters
|BE      |1407   |BE00001407|Elk        |0         | No voters
|BE      |2409   |BE00002409|Bobbie     |6         | No voters
|BE      |2632   |BE00002632|W2 - P632  |0         | No voters
|BE      |3003   |BE00003003|Benton East|0         | No voters
|BE      |6316   |BE00006316|316        |0         | No voters
|BE      |96     |BE00000096|Hanford 4  |0         | No voters
|BE      |97     |BE00000097|Hanford 3  |0         | No voters
|BE      |98     |BE00000098|Hanford 2  |0         | No voters
|BE      |99     |BE00000099|Hanford 1  |3         | No voters

[Grant](https://github.com/OpenPrecincts/WA18G/tree/master/geometries_missing_results_by_county/Grant%20County)
|CountyCd|PrcCode|FullPrc   |prec_name|population|reason    |
|--------|-------|----------|---------|----------|----------|
|GR      |0      |GR00000000|         |0         | No voters|

[Grays Harbor](https://github.com/OpenPrecincts/WA18G/tree/master/geometries_missing_results_by_county/GraysHarbor%20County)
|CountyCd|PrcCode|FullPrc   |prec_name  |population|reason    |
|--------|-------|----------|-----------|----------|----------|
|GY      |092    |GY00000092|Ocosta 092 |87        | No voters|
|GY      |603    |GY00000603|Montesano 603|0         | No voters|


[Lewis](https://github.com/OpenPrecincts/WA18G/tree/master/geometries_missing_results_by_county/Lewis%20County)
|CountyCd|PrcCode|FullPrc   |prec_name  |population|reason    |
|--------|-------|----------|-----------|----------|----------|
|LE      |20     |LE00000020|Fair       |0         | No Voters|
|LE      |27     |LE00000027|Jackson North|0         | No Voters|
|LE      |504    |LE00000504|Napavine #4|39        | No Voters|
|LE      |505    |LE00000505|Napavine #5|0         | No Voters|
|LE      |506    |LE00000506|Napavine #6|0         | No Voters|


[Okanogan](https://github.com/OpenPrecincts/WA18G/tree/master/geometries_missing_results_by_county/Okanogan%20County)
|CountyCd|PrcCode|FullPrc   |prec_name  |population|reason|
|--------|-------|----------|-----------|----------|------|
|OK      |227    |OK00000227|OKANOGAN AIRPORT|3         |Merged “OKANOGAN AIRPORT”/227 into “ELMWAY”/17|
|OK      |228    |OK00000228|BREWSTER AIRPORT|4         |Merged “BREWSTER AIRPORT”/228 into “BREWSTER FLAT”/179|
|OK      |229    |OK00000229|TONASKET AIRPORT|2         |Merged “TONASKET AIRPORT”/229 into “CAYUSE MTN”/156|
|OK      |230    |OK00000230|OMAK #27   |17        |Merged “OMAK”/230 into “WEST RIVER”/187|
|OK      |231    |OK00000231|OMAK RURAL |7         |Merged “OMAK RURAL”/231 into “OMAK #11”/203|
|OK      |232    |OK00000232|RODEO TRAIL #2|2         |Merged “RODEO TRAIL #2”/232 into “ELMWAY”/17|
|OK      |233    |OK00000233|RODEO TRAIL #3|0         |Merged “RODEO TRAIL #3”/233 into “ELMWAY”/17|
|OK      |234    |OK00000234|HORIZON    |21        |Merged “HORIZON”/234 into “WINTHROP #2”/137|
|OK      |235    |OK00000235|ISLAND     |7         |Merged “ISLAND”/235 into “OKANOGAN #13”/225|
|OK      |238    |OK00000238|OKANOGAN #16|97        |Merged “OKANOGAN #16”/238 into “FLETCHER”/200|
|OK      |26     |OK00000026|MONSE #2   |2         |Merged “MONSE #2”/26 into “MONSE #1”/25|
|OK      |28     |OK00000028|NIGHTHAWK  |26        |Merged “NIGHTHAWK”/28 into “PALMER LAKE”/69|
|OK      |300    |OK00000300|OKANOGAN #14|0         |Merged "OKANOGAN #14"/300 into “ELMWAY”/17|
|OK      |301    |OK00000301|OKANOGAN #15|0         |No Voters      |
|OK      |303    |OK00000303|OMAK #25   |19         |No Voters      |
|OK      |304    |OK00000304|OMAK #26   |0          |No Voters      |
|OK      |305    |OK00000305|OMAK AIRPORT|4         |No Voters      |
|OK      |306    |OK00000306|OMAK UNINCORPORATED|0  |No Voters      |
|OK      |307    |OK00000307|TWISP AIRPORT|6        |No Voters      |
|OK      |308    |OK00000308|OROVILLE AIRPORT|4     |No Voters      |
|OK      |309    |OK00000309|DEEP BAY   |2          |No Voters      |
|OK      |310    |OK00000310|WILDERNESS |0          |No Voters      |
|OK      |73     |OK00000073|SOUTH OMAK |5          |Merged “SOUTH OMAK”/73 into “OMAK”/212|
|OK      |80     |OK00000080|RODEO TRAIL #1|18        |Merged “RODEO TRAIL #1”/80 into “ELMWAY”/17|

[Pierce County](https://github.com/OpenPrecincts/WA18G/tree/master/geometries_missing_results_by_county/Pierce%20County)
|CountyCd|PrcCode|FullPrc   |prec_name|population estimate|reason|
|--------|-------|----------|---------|----------|----------|
|PI      |25-275 |PI00025275|25-275   |3         | No voters
|PI      |25-289 |PI00025289|25-289   |5         | No voters
|PI      |28-509 |PI00028509|28-509   |0         | No voters
|PI      |29-624 |PI00029624|29-624   |21        | No voters
|PI      |29-627 |PI00029627|29-627   |4         | No voters
|PI      |29-662 |PI00029662|29-662   |0         | No voters

[Snohomish county](https://github.com/OpenPrecincts/WA18G/tree/master/geometries_missing_results_by_county/Snohomish%20County)
|CountyCd|PrcCode |FullPrc   |prec_name|population|reason|
|--------|--------|----------|---------|----------|------|
|SN      |13918904|SN13918904|         |0         |No voters      |
|SN      |13918914|SN13918914|         |186       |No voters      |
|SN      |13958904|SN13958904|         |0         |No voters      |
|SN      |13958908|SN13958908|         |0         |No voters      |
|SN      |13958909|SN13958909|         |0         |No voters      |
|SN      |13958916|SN13958916|         |0         |No voters      |
|SN      |14428913|SN14428913|         |0         |No voters      |
|SN      |20131777|SN20131777|         |134       |No voters     |
|SN      |21018906|SN21018906|         |41        |No voters      |
|SN      |21018915|SN21018915|         |80        |No voters      |
|SN      |22128901|SN22128901|         |0         |No voters      |
|SN      |23244749|SN23244749|NILE     |3         |No voters   |
|SN      |23828903|SN23828903|         |0         |No voters      |
|SN      |23918902|SN23918902|         |0         |No voters      |
|SN      |23918906|SN23918906|         |10        |No voters      |
|SN      |23918907|SN23918907|         |8         |No voters      |
|SN      |23918911|SN23918911|         |0         |No voters      |
|SN      |24454591|SN24454591|SLIVER   |16        |No voters    |
|SN      |72138905|SN72138905|         |58        |No voters      |
|SN      |73238910|SN73238910|         |141       |No voters      |
|SN      |73238917|SN73238917|         |0         |No voters      |


[Walla Walla](https://github.com/OpenPrecincts/WA18G/tree/master/geometries_missing_results_by_county/WallaWalla%20County)
|CountyCd|PrcCode |FullPrc   |prec_name|population|reason|
|--------|--------|----------|---------|----------|------|
|WL      |30      |WL00000030|         |2         | No voters|


[Yakima County](https://github.com/OpenPrecincts/WA18G/tree/master/geometries_missing_results_by_county/Yakima%20County)
|CountyCd|PrcCode |FullPrc   |prec_name|population|reason|
|--------|--------|----------|---------|----------|------|
|YA      |160     |YA00000160|         |0         |No voters
|YA      |2100    |YA00002100|         |68        |No voters
|YA      |300     |YA00000300|         |0         |No voters
|YA      |3503    |YA00003503|         |2         |No voters
|YA      |900     |YA00000900|         |13        |No voters

### Election Results Missing Precinct Geomerties

`ELECTIONS OFFICE`: Contacted Kings County Board of Elections and learned the following:

> When a person who qualifies as service or overseas voter (referred to as UOCAVA voter) completes a voter registration, and the residential address is missing, we place voter in the ELECTIONS OFFICE precinct using the County Auditor’s Office address as required by WAC 434-235-020(c)(i). Only countywide offices, the congressional race in which the County Auditor’s Office is located, and ballot measures are counted. The ELECTIONS OFFICE precinct is only used for this purpose.
>
>After certification, the County Auditor must place the voter on inactive status, and then send a confirmation notice to obtain the correct residential address.

Accordingly, these votes could not be attributed to any specific precinct geometry.


|precinct|G18DStHou1|G18DStHou2|G18DStSen|G18DHOR|G18DSEN|G18IStHou1|G18IStHou2|G18IStSen|G18LStHou1|G18LStHou2|G18LStSen|G18LHOR|G18NPStHou1|G18NPStHou2|G18NPStSen|G18NPHOR|G18NPSEN|G18RStHou1|G18RStHou2|G18RStSen|G18RHOR|G18RSEN|loc_prec               |reason                                         |
|--------|----------|----------|---------|-------|-------|----------|----------|---------|----------|----------|---------|-------|-----------|-----------|----------|--------|--------|----------|----------|---------|-------|-------|-----------------------|-----------------------------------------------|
|Snohomish,1.02e+07 : SILER(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |SILER(*)               | Duplicate                                     |
|Snohomish,1.39e+07 : ARLINGTON 18(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |ARLINGTON 18(*)        |Duplicate                                      |
|Snohomish,1.39e+07 : GRANITE FALLS 3(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |GRANITE FALLS 3(*)     |Duplicate                                      |
|Snohomish,2.01e+07 : LYNNWOOD 27(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |LYNNWOOD 27(*)         |Duplicate                                      |
|Snohomish,2.32e+07 : LYNNWOOD 31(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |LYNNWOOD 31(*)         |Duplicate                                      |
|Snohomish,2.32e+07 : LYNNWOOD 32(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |LYNNWOOD 32(*)         |Duplicate                                      |
|Snohomish,2.32e+07 : MOUNTLAKE TERRACE 10(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |MOUNTLAKE TERRACE 10(*)|Duplicate                                      |
|Snohomish,2.32e+07 : NILE(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |NILE(*)                |Duplicate                                      |
|Snohomish,2.38e+07 : EVERETT  70(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |EVERETT  70(*)         |Duplicate                                      |
|Snohomish,2.38e+07 : LOMA(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |LOMA(*)                |Duplicate                                      |
|Snohomish,2.38e+07 : SPENCER(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |SPENCER(*)             |Duplicate                                      |
|Snohomish,2.38e+07 : TIMBER(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |TIMBER(*)              |Duplicate                                      |
|Snohomish,2.39e+07 : MARYSVILLE 33(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |MARYSVILLE 33(*)       |Duplicate                                      |
|Snohomish,2.45e+07 : GLEN ACRES(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |GLEN ACRES(*)          |Duplicate                                      |
|Snohomish,2.45e+07 : LANTERN(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |LANTERN(*)             |Duplicate                                      |
|Snohomish,2.45e+07 : SLIVER(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |SLIVER(*)              |Duplicate                                      |
|Whatcom,271 : 271|0.0       |3.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |Whatcom,271            | Precinct consolidated to protect voter privacy|
|Whatcom,271 : 271(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |Whatcom,271            | Duplicate                                     |
|Yakima,1 : 0001 - COUNTY COURTHOUSE(*)|0.0       |0.0       |0.0      |0.0    |0.0    |0.0       |0.0       |0.0      |0.0       |0.0       |0.0      |0.0    |0.0        |0.0        |0.0       |0.0     |0.0     |0.0       |0.0       |0.0      |0.0    |0.0    |Yakima,1               | Precinct consolidated to protect voter privacy|

# Washington Secretary of State 2018 Election Shapefile
In the process of creating this election shapefile, I was in touch with the office of Washington's Secretary of State. Through our correspondence I learned that they had prepared a file similar to what I had created. Aftering comparing my shapefile with theirs I found a number of difference within Okanogan County. 

Earlier in the process, I had reached out to Okanogan County Board of elections to inquire about a few precinct shapes that didn't have any election results. I learned that some precincts were combined with other precincts in that election in order to protect voter privacy in precincts with low turnout. They sent me a [spreadsheet](https://github.com/OpenPrecincts/WA18G/blob/master/geometries_missing_results_by_county/Okanogan%20County/Master%20Precinct%20List%20General%20Nov%206%2C02018.xlsx) detailing these aggregations which I executed in QGIS using the dissolve funciton. The Washington SOS's shapefile is missing such revisions, so I believe that this file is more accurate. 