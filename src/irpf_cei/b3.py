"""B3 module."""
import collections
import datetime
import sys
from typing import List


RatePeriod = collections.namedtuple("RatePeriod", ["start_date", "end_date", "rate"])

EMOLUMENTOS_PERIODS = [
    RatePeriod(
        datetime.datetime(2019, 1, 3), datetime.datetime(2019, 2, 1), 0.00004476
    ),
    RatePeriod(
        datetime.datetime(2019, 2, 4), datetime.datetime(2019, 3, 1), 0.00004032
    ),
    RatePeriod(
        datetime.datetime(2019, 3, 6), datetime.datetime(2019, 4, 1), 0.00004157
    ),
    RatePeriod(datetime.datetime(2019, 4, 2), datetime.datetime(2019, 5, 2), 0.0000408),
    RatePeriod(
        datetime.datetime(2019, 5, 3), datetime.datetime(2019, 6, 3), 0.00004408
    ),
    RatePeriod(
        datetime.datetime(2019, 6, 4), datetime.datetime(2019, 7, 1), 0.00004245
    ),
    RatePeriod(
        datetime.datetime(2019, 7, 2), datetime.datetime(2019, 8, 1), 0.00004189
    ),
    RatePeriod(
        datetime.datetime(2019, 8, 2), datetime.datetime(2019, 9, 2), 0.00004115
    ),
    RatePeriod(
        datetime.datetime(2019, 9, 3), datetime.datetime(2019, 10, 1), 0.00003756
    ),
    RatePeriod(
        datetime.datetime(2019, 10, 2), datetime.datetime(2019, 11, 1), 0.00004105
    ),
    RatePeriod(
        datetime.datetime(2019, 11, 4), datetime.datetime(2019, 12, 2), 0.0000411
    ),
    RatePeriod(
        datetime.datetime(2019, 12, 3), datetime.datetime(2020, 1, 1), 0.00003802
    ),
    RatePeriod(datetime.datetime(2020, 1, 1), datetime.datetime(2020, 2, 1), 0.0000366),
    RatePeriod(
        datetime.datetime(2020, 2, 1), datetime.datetime(2020, 3, 1), 0.00003462
    ),
    RatePeriod(
        datetime.datetime(2020, 3, 1), datetime.datetime(2020, 4, 1), 0.00003248
    ),
    RatePeriod(
        datetime.datetime(2020, 4, 1), datetime.datetime(2020, 5, 1), 0.00003006
    ),
    RatePeriod(datetime.datetime(2020, 5, 1), datetime.datetime(2020, 6, 3), 0.0000334),
    RatePeriod(
        datetime.datetime(2020, 6, 1), datetime.datetime(2020, 7, 1), 0.00003291
    ),
    RatePeriod(
        datetime.datetime(2020, 7, 1), datetime.datetime(2020, 8, 1), 0.00003089
    ),
    RatePeriod(datetime.datetime(2020, 8, 1), datetime.datetime(2020, 9, 1), 0.0000318),
    RatePeriod(
        datetime.datetime(2020, 9, 1), datetime.datetime(2020, 10, 1), 0.00003125
    ),
    RatePeriod(
        datetime.datetime(2020, 10, 1), datetime.datetime(2020, 11, 1), 0.00003219
    ),
    RatePeriod(
        datetime.datetime(2020, 11, 1), datetime.datetime(2020, 12, 1), 0.00003247
    ),
    RatePeriod(
        datetime.datetime(2020, 12, 1), datetime.datetime(2021, 1, 1), 0.00003020
    ),
]
EMOLUMENTOS_AUCTION_RATE = 0.00007
LIQUIDACAO_RATE = 0.000275

AssetInfo = collections.namedtuple("AssetInfo", ["category", "cnpj"])

ETFS = {
    "BBSD": "17.817.528/0001-50",
    "XBOV": "14.120.533/0001-11",
    "BOVB": "32.203.211/0001-18",
    "IVVB": "19.909.560/0001-91",
    "BOVA": "10.406.511/0001-61",
    "BRAX": "11.455.378/0001-04",
    "ECOO": "15.562.377/0001-01",
    "SMAL": "10.406.600/0001-08",
    "BOVV": "21.407.758/0001-19",
    "DIVO": "13.416.245/0001-46",
    "FIND": "11.961.094/0001-81",
    "GOVE": "11.184.136/0001-15",
    "MATB": "13.416.228/0001-09",
    "ISUS": "12.984.444/0001-98",
    "PIBB": "06.323.688/0001-27",
    "SMAC": "34.803.814/0001-86",
    "SPXI": "17.036.289/0001-00",
}
FIIS = {
    "ALZR": "28.737.771/0001-85",
    "AQLL": "13.555.918/0001-49",
    "BCRI": "22.219.335/0001-38",
    "BNFS": "15.570.431/0001-60",
    "BBPO": "14.410.722/0001-29",
    "BBIM": "20.716.161/0001-93",
    "BBRC": "12.681.340/0001-04",
    "RDPD": "23.120.027/0001-13",
    "RNDP": "15.394.563/0001-89",
    "BCIA": "20.216.935/0001-17",
    "BZLI": "14.074.706/0001-02",
    "CARE": "13.584.584/0001-31",
    "BRCO": "20.748.515/0001-81",
    "BTLG": "11.839.593/0001-09",
    "CRFF": "31.887.401/0001-39",
    "CXRI": "17.098.794/0001-70",
    "CPFF": "34.081.611/0001-23",
    "CBOP": "17.144.039/0001-85",
    "GRLV": "17.143.998/0001-86",
    "HGFF": "32.784.898/0001-22",
    "HGLG": "11.728.688/0001-47",
    "HGPO": "11.260.134/0001-68",
    "HGRE": "09.072.017/0001-29",
    "HGCR": "11.160.521/0001-22",
    "HGRU": "29.641.226/0001-53",
    "ERPA": "31.469.385/0001-64",
    "KINP": "24.070.076/0001-51",
    "VRTA": "11.664.201/0001-00",
    "BMII": "02.027.437/0001-44",
    "BTCR": "29.787.928/0001-40",
    "FAED": "11.179.118/0001-45",
    "BPRP": "29.800.650/0001-01",
    "BRCR": "08.924.783/0001-01",
    "FEXC": "09.552.812/0001-14",
    "BCFF": "11.026.627/0001-38",
    "FCFL": "11.602.654/0001-01",
    "CNES": "13.551.286/0001-45",
    "CEOC": "15.799.397/0001-09",
    "THRA": "13.966.653/0001-71",
    "EDGA": "15.333.306/0001-37",
    "FLRP": "10.375.382/0001-91",
    "HCRI": "04.066.582/0001-60",
    "NSLU": "08.014.513/0001-63",
    "HTMX": "08.706.065/0001-69",
    "MAXR": "11.274.415/0001-70",
    "NCHB": "18.085.673/0001-57",
    "NVHO": "17.025.970/0001-44",
    "PQDP": "10.869.155/0001-12",
    "PRSV": "11.281.322/0001-72",
    "RBRM": "26.314.437/0001-93",
    "RBRR": "29.467.977/0001-03",
    "JRDM": "14.879.856/0001-93",
    "TBOF": "17.365.105/0001-47",
    "ALMI": "07.122.725/0001-00",
    "TRNT": "04.722.883/0001-02",
    "RECT": "32.274.163/0001-59",
    "UBSR": "28.152.272/0001-26",
    "VLOL": "15.296.696/0001-12",
    "OUFF": "30.791.386/0001-68",
    "VVPR": "33.045.581/0001-37",
    "LVBI": "30.629.603/0001-18",
    "BARI": "29.267.567/0001-00",
    "BBVJ": "10.347.985/0001-80",
    "BPFF": "17.324.357/0001-28",
    "BVAR": "21.126.204/0001-43",
    "BPML": "33.046.142/0001-49",
    "CXTL": "12.887.506/0001-43",
    "CTXT": "00.762.723/0001-28",
    "FLMA": "04.141.645/0001-03",
    "EURO": "05.437.916/0001-27",
    "FIGS": "17.590.518/0001-25",
    "ABCP": "01.201.140/0001-90",
    "GTWR": "23.740.527/0001-58",
    "HBTT": "26.846.202/0001-42",
    "HUSC": "28.851.767/0001-43",
    "FIIB": "14.217.108/0001-45",
    "FINF": "18.369.510/0001-04",
    "FMOF": "01.633.741/0001-72",
    "MBRF": "13.500.306/0001-59",
    "MGFF": "29.216.463/0001-77",
    "NPAR": "24.814.916/0001-43",
    "PABY": "00.613.094/0001-74",
    "FPNG": "17.161.979/0001-82",
    "VPSI": "14.721.889/0001-00",
    "FPAB": "03.251.720/0001-18",
    "RBRY": "30.166.700/0001-11",
    "RBRP": "21.408.063/0001-51",
    "RCRB": "03.683.056/0001-86",
    "RBED": "13.873.457/0001-52",
    "RBVA": "15.576.907/0001-70",
    "RNGO": "15.006.286/0001-90",
    "SFND": "09.350.920/0001-04",
    "FISC": "12.804.013/0001-00",
    "SCPF": "01.657.856/0001-05",
    "SDIL": "16.671.412/0001-93",
    "SHPH": "03.507.519/0001-59",
    "TGAR": "25.032.881/0001-53",
    "ONEF": "12.948.291/0001-23",
    "TOUR": "30.578.316/0001-26",
    "FVBI": "13.022.993/0001-44",
    "VERE": "08.693.497/0001-82",
    "FVPQ": "00.332.266/0001-31",
    "FIVN": "17.854.016/0001-64",
    "VTLT": "27.368.600/0001-63",
    "VSHO": "23.740.595/0001-17",
    "IBFF": "33.721.517/0001-29",
    "PLCR": "32.527.683/0001-26",
    "CVBI": "28.729.197/0001-13",
    "MCCI": "23.648.935/0001-84",
    "ARRI": "32.006.821/0001-21",
    "HOSI": "34.081.631/0001-02",
    "IRDM": "28.830.325/0001-10",
    "KFOF": "30.091.444/0001-40",
    "OUCY": "28.516.650/0001-03",
    "GSFI": "11.769.604/0001-13",
    "GGRC": "26.614.291/0001-00",
    "RCFA": "27.771.586/0001-44",
    "HABT": "30.578.417/0001-05",
    "ATCR": "14.631.148/0001-39",
    "HCTR": "30.248.180/0001-96",
    "ATSA": "12.809.972/0001-00",
    "HGBS": "08.431.747/0001-06",
    "HLOG": "27.486.542/0001-72",
    "HRDF": "16.929.519/0001-99",
    "HPDP": "35.586.415/0001-73",
    "HMOC": "14.733.211/0001-48",
    "HFOF": "18.307.582/0001-19",
    "TFOF": "20.834.884/0001-97",
    "HSML": "32.892.018/0001-31",
    "BICR": "34.007.109/0001-72",
    "RBBV": "16.915.868/0001-51",
    "JPPA": "30.982.880/0001-00",
    "JPPC": "17.216.625/0001-98",
    "JSRE": "13.371.132/0001-71",
    "JTPR": "23.876.086/0001-16",
    "KNHY": "30.130.708/0001-28",
    "KNRE": "14.423.780/0001-97",
    "KNIP": "24.960.430/0001-13",
    "KNRI": "12.005.956/0001-65",
    "KNCR": "16.706.958/0001-32",
    "LGCP": "34.598.181/0001-11",
    "LUGG": "34.835.191/0001-23",
    "DMAC": "30.579.348/0001-46",
    "MALL": "26.499.833/0001-32",
    "MXRF": "97.521.225/0001-25",
    "MFII": "16.915.968/0001-88",
    "PRTS": "22.957.521/0001-74",
    "SHOP": "22.459.737/0001-00",
    "NEWL": "32.527.626/0001-47",
    "OUJP": "26.091.656/0001-50",
    "ORPD": "19.107.604/0001-60",
    "PATC": "30.048.651/0001-12",
    "PLRI": "14.080.689/0001-16",
    "PORD": "17.156.502/0001-09",
    "PBLV": "31.962.875/0001-06",
    "QAGR": "32.754.734/0001-52",
    "RSPD": "19.249.989/0001-08",
    "RBDS": "11.945.604/0001-27",
    "RBGS": "13.652.006/0001-95",
    "RBCO": "31.894.369/0001-19",
    "RBRD": "09.006.914/0001-34",
    "RBTS": "29.299.737/0001-39",
    "RBRF": "27.529.279/0001-51",
    "DOMC": "17.374.696/0001-19",
    "RBVO": "15.769.670/0001-44",
    "RBFF": "17.329.029/0001-14",
    "SAAG": "16.915.840/0001-14",
    "SADI": "32.903.521/0001-45",
    "SARE": "32.903.702/0001-71",
    "FISD": "16.543.270/0001-89",
    "WPLZ": "09.326.861/0001-39",
    "REIT": "16.841.067/0001-99",
    "SPTW": "15.538.445/0001-05",
    "SPAF": "18.311.024/0001-27",
    "STRX": "11.044.355/0001-07",
    "TSNC": "17.007.443/0001-07",
    "TCPF": "26.990.011/0001-50",
    "XTED": "15.006.267/0001-63",
    "TRXF": "28.548.288/0001-52",
    "VGIR": "29.852.732/0001-91",
    "VLJS": "13.842.683/0001-76",
    "VILG": "24.853.044/0001-22",
    "VINO": "12.516.185/0001-70",
    "VISC": "17.554.274/0001-25",
    "VOTS": "17.870.926/0001-30",
    "XPCM": "16.802.320/0001-03",
    "XPCI": "28.516.301/0001-91",
    "XPHT": "18.308.516/0001-63",
    "XPIN": "28.516.325/0001-40",
    "XPLG": "26.502.794/0001-85",
    "XPML": "28.757.546/0001-00",
    "XPPR": "30.654.849/0001-40",
    "XPSF": "30.983.020/0001-90",
    "YCHY": "28.267.696/0001-36",
    "ARFI": "14.069.202/0001-02",
    "BBFI": "07.000.400/0001-46",
    "CPTS": "18.979.895/0001-13",
    "DAMT": "26.642.727/0001-66",
    "DOVL": "10.522.648/0001-81",
    "ANCR": "07.789.135/0001-27",
    "BMLC": "14.376.247/0001-11",
    "FAMB": "05.562.312/0001-02",
    "ELDO": "13.022.994/0001-99",
    "SHDP": "07.224.019/0001-60",
    "SAIC": "17.311.079/0001-74",
    "WTSP": "28.693.595/0001-27",
    "BRHT": "15.461.076/0001-91",
    "CXCE": "10.991.914/0001-15",
    "EDFO": "06.175.262/0001-73",
    "GESE": "17.007.528/0001-95",
    "OULG": "13.974.819/0001-00",
    "LATR": "17.209.378/0001-00",
    "LOFT": "19.722.048/0001-31",
    "DRIT": "10.456.810/0001-00",
    "NVIF": "22.003.469/0001-17",
    "FTCE": "01.235.622/0001-61",
    "PRSN": "14.056.001/0001-62",
    "FIIP": "08.696.175/0001-97",
    "RCRI": "26.511.274/0001-39",
    "FOFT": "16.875.388/0001-04",
}
STOCKS = {
    "AALR3": "42.771.949/0001-35",
    "ABCB4": "28.195.667/0001-06",
    "ABEV3": "07.526.557/0001-00",
    "ADHM3": "10.345.009/0001-98",
    "AGRO3": "07.628.528/0001-59",
    "ALPA3": "61.079.117/0001-05",
    "ALPA4": "61.079.117/0001-05",
    "ALSC3": "06.082.980/0001-03",
    "ALUP11": "08.364.948/0001-38",
    "ALUP3": "08.364.948/0001-38",
    "ALUP4": "08.364.948/0001-38",
    "AMAR3": "61.189.288/0001-89",
    "ANIM3": "09.288.252/0001-32",
    "ARZZ3": "16.590.234/0001-76",
    "ATOM3": "00.359.742/0001-08",
    "AZUL4": "09.305.994/0001-29",
    "B3SA3": "09.346.601/0001-25",
    "BAUH3": "95.426.862/0001-97",
    "BAUH4": "95.426.862/0001-97",
    "BBAS3": "00.000.000/0001-91",
    "BBDC3": "60.746.948/0001-12",
    "BBDC4": "60.746.948/0001-12",
    "BBRK3": "08.613.550/0001-98",
    "BBSE3": "17.344.597/0001-94",
    "BEEF3": "67.620.377/0001-14",
    "BIDI4": "18.945.670/0001-46",
    "BIDI11": "18.945.670/0001-46",
    "BOBR3": "50.564.053/0001-03",
    "BOBR4": "50.564.053/0001-03",
    "BPAC11": "30.306.294/0001-45",
    "BPAC3": "30.306.294/0001-45",
    "BPAC5": "30.306.294/0001-45",
    "BPAN4": "59.285.411/0001-13",
    "BPHA3": "11.395.624/0001-71",
    "BRAP3": "03.847.461/0001-92",
    "BRAP4": "03.847.461/0001-92",
    "BRDT3": "34.274.233/0001-02",
    "BRFS3": "01.838.723/0001-27",
    "BRIN3": "11.721.921/0001-60",
    "BRKM3": "42.150.391/0001-70",
    "BRKM5": "42.150.391/0001-70",
    "BRKM6": "42.150.391/0001-70",
    "BRML3": "06.977.745/0001-91",
    "BRPR3": "06.977.751/0001-49",
    "BMGB4": "61.186.680/0001-74",
    "BRSR3": "92.702.067/0001-96",
    "BRSR5": "92.702.067/0001-96",
    "BRSR6 ": "92.702.067/0001-96",
    "BSEV3": "15.527.906/0001-36",
    "BTOW3": "00.776.574/0001-56",
    "CAML3": "64.904.295/0001-03",
    "CARD3": "01.896.779/0001-38",
    "CCRO3": "02.846.056/0001-97",
    "CCXC3": "07.950.674/0001-04",
    "CEPE3": "10.835.932/0001-08",
    "CEPE5": "10.835.932/0001-08",
    "CEPE6": "10.835.932/0001-08",
    "CESP3": "60.933.603/0001-78",
    "CESP5": "60.933.603/0001-78",
    "CESP6": "60.933.603/0001-78",
    "CGAS3": "61.856.571/0001-17",
    "CGAS5": "61.856.571/0001-17",
    "CGRA3": "92.012.467/0001-70",
    "CGRA4": "92.012.467/0001-70",
    "CIEL3": "01.027.058/0001-91",
    "CMIG3": "17.155.730/0001-64",
    "CMIG4": "17.155.730/0001-64",
    "CNTO3": "13.217.485/0001-11",
    "COCE3": "07.047.251/0001-70",
    "COCE5": "07.047.251/0001-70",
    "COCE6": "07.047.251/0001-70",
    "CPFE3": "02.429.144/0001-93",
    "CREM3": "82.641.325/0001-18",
    "CRFB3": "75.315.333/0001-09",
    "CSAN3": "50.746.577/0001-15",
    "CSMG3": "17.281.106/0001-03",
    "CSNA3": "33.042.730/0001-04",
    "CEAB3": "45.242.914/0001-05",
    "CTKA3": "82.640.558/0001-04",
    "CTKA4": "82.640.558/0001-04",
    "CTNM3": "22.677.520/0001-76",
    "CTNM4": "22.677.520/0001-76",
    "CVCB3": "10.760.260/0001-19",
    "CYRE3": "73.178.600/0001-18",
    "DAGB33": "11.423.623/0001-93",
    "DIRR3": "16.614.075/0001-00",
    "DMMO3": "08.926.302/0001-05",
    "DTEX3": "97.837.181/0001-47",
    "ECOR3": "04.149.454/0001-80",
    "EGIE3": "02.474.103/0001-19",
    "ELEK3": "13.788.120/0001-47",
    "ELEK4": "13.788.120/0001-47",
    "ELPL3": "61.695.227/0001-93",
    "ELET3": "00.001.180/0001-26",
    "ELET6": "00.001.180/0001-26",
    "EMBR3": "07.689.002/0001-89",
    "ENBR3": "03.983.431/0001-03",
    "ENEV3": "04.423.567/0001-21",
    "ENGI11": "00.864.214/0001-06",
    "ENGI3": "00.864.214/0001-06",
    "ENGI4": "00.864.214/0001-06",
    "EQTL3": "03.220.438/0001-73",
    "YDUQ3": "08.807.432/0001-10",
    "ESTR3": "61.082.004/0001-50",
    "ESTR4": "61.082.004/0001-50",
    "ETER3": "61.092.037/0001-81",
    "EUCA3": "56.643.018/0001-66",
    "EUCA4": "56.643.018/0001-66",
    "EVEN3": "43.470.988/0001-65",
    "EZTC3": "08.312.229/0001-73",
    "FESA3": "15.141.799/0001-03",
    "FESA4": "15.141.799/0001-03",
    "FHER3": "22.266.175/0001-88",
    "TASA3": "92.781.335/0001-02",
    "TASA4": "92.781.335/0001-02",
    "FJTA3": "92.781.335/0001-02",
    "FJTA4": "92.781.335/0001-02",
    "FLRY3": "60.840.055/0001-31",
    "FRAS3": "88.610.126/0001-29",
    "GNDI3": "19.853.511/0001-84",
    "HAPV3": "63.554.067/0001-98",
    "FRIO3": "04.821.041/0001-08",
    "GEPA3": "02.998.301/0001-81",
    "GEPA4": "02.998.301/0001-81",
    "GFSA3": "01.545.826/0001-07",
    "GGBR3": "33.611.500/0001-19",
    "GGBR4": "33.611.500/0001-19",
    "GOAU3": "92.690.783/0001-09",
    "GOAU4": "92.690.783/0001-09",
    "GOLL4": "06.164.253/0001-87",
    "GRND3": "89.850.341/0001-60",
    "GSHP3": "08.764.621/0001-53",
    "GUAR3": "08.402.943/0001-52",
    "GUAR4": "08.402.943/0001-52",
    "HBOR3": "49.263.189/0001-02",
    "HGTX3": "78.876.950/0001-71",
    "HYPE3": "02.932.074/0001-91",
    "HOOT3": "33.200.049/0001-47",
    "HOOT4": "33.200.049/0001-47",
    "IDNT3": "02.365.069/0001-44",
    "IGTA3": "51.218.147/0001-93",
    "IRBR3": "33.376.989/0001-91",
    "ITSA3": "61.532.644/0001-15",
    "ITSA4": "61.532.644/0001-15",
    "ITUB3": "60.872.504/0001-23",
    "ITUB4": "60.872.504/0001-23",
    "JBSS3": "02.916.265/0001-60",
    "JHSF3": "08.294.224/0001-65",
    "JSLG3": "52.548.435/0001-79",
    "KEPL3": "91.983.056/0001-69",
    "KLBN11": "89.637.490/0001-45",
    "KLBN3": "89.637.490/0001-45",
    "KLBN4": "89.637.490/0001-45",
    "COGN3": "02.800.026/0001-40",
    "KROT3": "02.800.026/0001-40",
    "LAME3": "33.014.556/0001-96",
    "LAME4": "33.014.556/0001-96",
    "LCAM3": "10.215.988/0001-60",
    "LEVE3": "60.476.884/0001-87",
    "LIGT3": "03.378.521/0001-75",
    "LINX3": "06.948.969/0001-75",
    "LLIS3": "49.669.856/0001-43",
    "LIQO3": "04.032.433/0001-80",
    "LOGG3": "09.041.168/0001-10",
    "LOGN3": "42.278.291/0001-24",
    "LPSB3": "08.078.847/0001-09",
    "LREN3": "92.754.738/0001-62",
    "LUPA3": "89.463.822/0001-12",
    "MAGG3": "08.684.547/0001-65",
    "MDIA3": "07.206.816/0001-15",
    "MGLU3": "47.960.950/0001-21",
    "MILS3": "27.093.558/0001-15",
    "MMXM3": "02.762.115/0001-49",
    "MNDL3": "88.610.191/0001-54",
    "MOVI3": "21.314.559/0001-66",
    "MPLU3": "11.094.546/0001-75",
    "MRFG3": "03.853.896/0001-40",
    "MRVE3": "08.343.492/0001-20",
    "MULT3": "07.816.890/0001-53",
    "MYPK3": "61.156.113/0001-75",
    "NAFG3": "61.067.161/0001-97",
    "NAFG4": "61.067.161/0001-97",
    "NATU3": "71.673.990/0001-77",
    "ODPV3": "58.119.199/0001-51",
    "OFSA3": "20.258.278/0001-70",
    "OIBR3": "76.535.764/0001-43",
    "OIBR4": "76.535.764/0001-43",
    "OSXB3": "09.112.685/0001-32",
    "PARD3": "19.378.769/0001-76",
    "PCAR3": "47.508.411/0001-56",
    "PCAR4": "47.508.411/0001-56",
    "PDGR3": "02.950.811/0001-89",
    "PETR3": "33.000.167/0001-01",
    "PETR4": "33.000.167/0001-01",
    "PFRM3": "45.453.214/0001-51",
    "PINE3": "62.144.175/0001-20",
    "PINE4": "62.144.175/0001-20",
    "PMAM3": "60.398.369/0004-79",
    "POMO3": "88.611.835/0001-29",
    "POMO4": "88.611.835/0001-29",
    "POSI3": "81.243.735/0001-48",
    "PRIO3": "10.629.105/0001-68",
    "PRML3": "08.741.499/0001-08",
    "PSSA3": "02.149.205/0001-69",
    "QGEP3": "11.669.021/0001-10",
    "QUAL3": "11.992.680/0001-93",
    "RADL3": "61.585.865/0001-51",
    "RAIL3": "02.387.241/0001-60",
    "RAPT3": "89.086.144/0001-16",
    "RAPT4": "89.086.144/0001-16",
    "RCSL3": "91.333.666/0001-17",
    "RCSL4": "91.333.666/0001-17",
    "REDE3": "61.584.140/0001-49",
    "RENT3": "16.670.085/0001-55",
    "RNEW11": "08.534.605/0001-74",
    "RNEW3": "08.534.605/0001-74",
    "RNEW4": "08.534.605/0001-74",
    "ROMI3": "56.720.428/0001-63",
    "RPMG3": "33.412.081/0001-96",
    "RSID3": "61.065.751/0001-80",
    "SANB11": "90.400.888/0001-42",
    "SANB3": "90.400.888/0001-42",
    "SANB4": "90.400.888/0001-42",
    "SAPR11": "76.484.013/0001-45",
    "SAPR3": "76.484.013/0001-45",
    "SAPR4": "76.484.013/0001-45",
    "SBSP3": "43.776.517/0001-80",
    "SCAR3": "29.780.061/0001-09",
    "SEDU3": "02.541.982/0001-54",
    "SEER3": "04.986.320/0001-13",
    "SGPS3": "07.718.269/0001-57",
    "SHOW3": "02.860.694/0001-62",
    "SHUL3": "84.693.183/0001-68",
    "SHUL4": "84.693.183/0001-68",
    "SLCE3": "89.096.457/0001-55",
    "SLED3": "60.500.139/0001-26",
    "SLED4": "60.500.139/0001-26",
    "SMLS3": "05.730.375/0001-20",
    "SMTO3": "51.466.860/0001-56",
    "SQIA3": "04.065.791/0001-99",
    "SNSL3": "04.065.791/0001-99",
    "SSBR3": "05.878.397/0001-32",
    "STBP3": "02.762.121/0001-04",
    "SULA11": "29.978.814/0001-87",
    "SULA3": "29.978.814/0001-87",
    "SULA4": "29.978.814/0001-87",
    "SUZB3": "16.404.287/0001-55",
    "TAEE11": "07.859.971/0001-30",
    "TAEE3": "07.859.971/0001-30",
    "TAEE4": "07.859.971/0001-30",
    "TCNO3": "33.111.246/0001-90",
    "TCNO4": "33.111.246/0001-90",
    "TCSA3": "08.065.557/0001-12",
    "TECN3": "09.295.063/0001-97",
    "TEKA3": "82.636.986/0001-55",
    "TEKA4": "82.636.986/0001-55",
    "TEND3": "71.476.527/0001-35",
    "TGMA3": "02.351.144/0001-18",
    "TIET11": "04.128.563/0001-10",
    "TIET3": "04.128.563/0001-10",
    "TIET4": "04.128.563/0001-10",
    "TIMP3": "02.558.115/0001-21",
    "TOTS3": "53.113.791/0001-22",
    "TOYB3": "22.770.366/0001-82",
    "TOYB4": "22.770.366/0001-82",
    "TPIS3": "03.014.553/0001-91",
    "TRIS3": "08.811.643/0001-27",
    "TRPL3": "02.998.611/0001-04",
    "TRPL4": "02.998.611/0001-04",
    "TRPN3": "05.341.549/0001-63",
    "TUPY3": "84.683.374/0001-49",
    "UCAS3": "90.441.460/0001-48",
    "UGPA3": "33.256.439/0001-39",
    "UNIP6": "33.958.695/0001-78",
    "USIM3": "60.894.730/0001-05",
    "USIM5": "60.894.730/0001-05",
    "USIM6": "60.894.730/0001-05",
    "VALE3": "33.592.510/0001-54",
    "VIVA3": "84.453.844/0342-44",
    "VIVR3": "67.571.414/0001-41",
    "VIVT3": "02.558.157/0001-62",
    "VIVT4": "02.558.157/0001-62",
    "VLID3": "33.113.309/0001-47",
    "VULC3": "50.926.955/0001-42",
    "VVAR11": "33.041.260/0652-90",
    "VVAR3": "33.041.260/0652-90",
    "VVAR4": "33.041.260/0652-90",
    "WEGE3": "84.429.695/0001-11",
    "WHRL3": "59.105.999/0001-86",
    "WHRL4": "59.105.999/0001-86",
    "WIZS3": "42.278.473/0001-03",
    "WSON33": "05.721.735/0001-28",
    "NEOE3": "01.083.200/0001-18",
    "TELB3": "00.336.701/0001-04",
    "TELB4": "00.336.701/0001-04",
    "BEES3": "28.127.603/0001-78",
    "BEES4": "28.127.603/0001-78",
    "EALT4": "82.643.537/0001-34",
    "MEAL3": "17.314.329/0001-20",
    "PTNT4": "88.613.658/0001-10",
    "JPSA3": "60.543.816/0001-93",
    "ENAT3": "11.669.021/0001-10",
    "CRPG5": "15.115.504/0001-24",
    "BKBR3": "13.574.594/0001-96",
    "GBIO33": "19.688.956/0001-56",
    "PTBL3": "83.475.913/0001-91",
    "ALSO3": "05.878.397/0001-32",
    "BMEB4": "17.184.037/0001-10",
    "BTTL3": "42.331.462/0001-31",
    "FRTA3": "86.550.951/0001-50",
    "TESA3": "05.799.312/0001-20",
    "MNPR3": "90.076.886/0001-40",
    "AZEV4": "61.351.532/0001-68",
    "NTCO3": "32.785.497/0001-97",
}

CNPJ_INSTITUTIONS = {
    "39": "74.014.747/0001-35",
    "4": "62.178.421/0001-64",
    "226": "17.312.661/0001-55",
    "147": "33.775.974/0001-04",
    "1982": "30.723.886/0001-62",
    "172": "93.026.847/0001-26",
    "72": "61.855.045/0001-32",
    "120": "05.816.451/0001-15",
    "85": "43.815.158/0001-22",
    "308": "02.332.886/0011-78",
    "88": "02.685.483/0001-30",
    "234": "09.512.542/0001-18",
    "74": "00.336.036/0001-40",
    "45": "42.584.318/0001-07",
    "90": "62.169.875/0001-79",
    "174": "28.048.783/0001-00",
    "131": "63.062.749/0001-83",
    "173": "27.652.684/0001-62",
    "186": "92.858.380/0001-18",
    "15": "65.913.436/0001-17",
    "115": "01.788.147/0001-50",
    "54": "33.894.445/0001-11",
    "735": "09.105.360/0001-22",
    "1099": "18.945.670/0001-46",
    "114": "61.194.353/0001-64",
    "16": "32.588.139/0001-94",
    "106": "16.683.062/0001-85",
    "13": "02.670.590/0001-95",
    "262": "12.392.983/0001-38",
    "40": "04.323.351/0001-94",
    "23": "52.904.364/0001-08",
    "93": "04.257.795/0001-79",
    "63": "43.060.029/0001-71",
    "129": "00.806.535/0001-54",
    "386": "02.332.886/0016-82",
    "3762": "42.066.258/0001-30",
    "59": "60.783.503/0001-02",
    "27": "51.014.223/0001-49",
    "187": "17.315.359/0001-50",
    "58": "62.285.390/0001-40",
    "177": "68.757.681/0001-70",
    "10": "61.739.629/0001-42",
    "107": "03.751.794/0001-13",
    "4090": "29.162.769/0001-98",
    "37": "33.968.066/0001-29",
    "29": "28.156.214/0001-70",
    "21": "03.384.738/0001-98",
    "3": "02.332.886/0001-04",
}


def get_asset_info(code: str) -> AssetInfo:
    """Return asset info.

    Args:
        code: asset code.

    Returns:
        AssetInfo: category and cnpj.
    """
    if code in STOCKS:
        return AssetInfo("STOCKS", STOCKS[code])
    # ETF and FII code can end in 11 or 11B
    if len(code) == 6 and code.endswith("11"):
        code = code[:-2]
    elif len(code) == 7 and code.endswith("11B"):
        code = code[:-3]
    if code in FIIS:
        return AssetInfo("FII", FIIS[code])
    if code in ETFS:
        return AssetInfo("ETF", ETFS[code])
    return AssetInfo("NOT_FOUND", "")


def get_trading_rate() -> float:
    """Return fixes trading rate.

    Returns:
        float: constant float.
    """
    return LIQUIDACAO_RATE


def get_emoluments_rates(
    dates: List[datetime.datetime], auction_trades: List[int]
) -> List[float]:
    """Get the list of emuluments rates.

    Args:
        dates (List[datetime.datetime]): list of trade days.
        auction_trades (List[int]): list of indexes of trades in auction.

    Returns:
        List[float]: list of rates.
    """
    rates = []
    last_period = 0
    for date in dates:
        for idx_period, period in enumerate(
            EMOLUMENTOS_PERIODS[last_period:], start=last_period
        ):
            if period.start_date <= date <= period.end_date:
                last_period = idx_period
                rates.append(period.rate)
                break
        else:
            sys.exit(f"Nenhum período de emolumentos encontrado para a data: {date}")
    for trade in auction_trades:
        rates[trade] = EMOLUMENTOS_AUCTION_RATE
    return rates


def get_cnpj_institution(institution: str) -> str:
    """Return CNPJ of institution.

    Args:
        institution (str): full institution description.

    Returns:
        str: CNPJ or not found message.
    """
    b3_code = institution.split(" - ")[0]
    if b3_code in CNPJ_INSTITUTIONS:
        return CNPJ_INSTITUTIONS[b3_code]
    return "não encontrado"
