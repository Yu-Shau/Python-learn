#   条件1:密码是小写字母
#   条件2:密码两端有且仅有3个大写字母(超过3个的不是密码)
str1 = """
ACFlCTLIQlAIVMTqHFkswqbDDHtpgcWaXSSglUYKE
lqNsYCyaQXBzrFUbkAUAWAKrDgDtAlGMBqWQhpEwquZqWZJpslUfMllCwWptqINjrOBTLuPzwvXNbLCx
oFRritKRpJgBOaGPZdkUzvYnvYmAlEsVmKRXqyQUOdCBqLYyboOYeAQNLnkuiDXCiNiksSSRpDMVQQgs
TmYThnppfKSmkpjjceGLaMOvYgsvNkGENKgGtUSzVPlLMeephDKrWGNpAxBqRiCnQIuKwDZurIRsznUp
xhstMWpHdZzqeEnttlAHiWbhbIJpwKBAGsFWthBiwBDKTFzIUamELZJFLbmqOmwBIYBJIofAUyxTLUEm
LcOXzjIHFcfUfEWccbWzhVuIZMdTVsOaNsLTpHjrvFaYTnJUrqaYnUmbobfOXXtkjKjFUEhVNlPWeaIY
uABNuEDKFWiUaqQiBHGsgEmDSKiJKLkkzFWlobXIyUlDzGcwDnEOwwWxgFpebsslmKItazIYctPROSJp
ImDHusQIkoFQSmuqwdcPNERvflfHtkGTrtbQXqZUsazoxmbVTPIuuxKvfALAaGnIuIZwczCcoIRMncBs
timFGHPJPaHMPTLjsBjIwbbzKyghaDTUStzJceaYAneywwpvdiUJifPHtXmAwZPChWsDmwonzeeQCEiB
xWsJLAtrdVEOBxEaYiSabHdUwlXlDOAKzZUwozJoBGvnFttDkXdYdjQSzzhTIPfYpWVFdiFIqSbyPZIi
VoXunBPbAJVMWluPcIfHmjPeHaTyClCvTOucEYEZXbVDiZMsfeuruDGMmQEsHutzvzVmWvCoPRguBiHh
taTeaguPmNuAxzYJLEcdoApfIFBaLUqettjTJNlHZYlJZRRoKXEvFnoUHdPjDuXuTAubGODkHAokpItw
SlEwhjrUSlfMawWlTMciWAzVcgPcqCHIaogokYAWGsvWZzBfJqzxIkCNvHDvBkOMCyeYXzVVuRJLQIOy
BMoVPgFLOagDxyPfWxTtZQNCLOrVVclPzMNYruNUyMOBKxBvinxuGMAAfndhPsROtkOJAAJQSxpmTzXm
CmEwZOhlItvETUneqvdKLghLyREjuJWRFjVVuNMiPuvvmRaEUmjCXDVuMRAvBuHUYGKPXthWISIbueRp
uvxpmqclmrXpAGFrxhJGxQwlrbkHEmcEUooCoPqGzbrCfIWmtUKmzzXvcqbhxKcAwXCNjbJDWDndKiLK
HwaFKyhXJQgHjIaTfIJrkhUpTHJZebRertDigQtDKxGerMRgHWFTrqqZlcBjAUfTZdFlZCAEZnhzgTIy
gJSsWJjFcCVoFonAfKPTOhTxjxTRtzSKLoIOScEwBCDvWFDVGpBOpijqdwvugoYsyuIOZJTcySDrzy
wBxediHOIYgasrUIDsNZcParqTGfTaBZHoSssXGtiCVvLReyoiitzMpsouqUeMHGWwDMgBaQTRkxPwNP
XsvyFVXfjgKuamMTsEsbeKDgAdVndyDleenPBcXWKGPcDsALDajkCEGufvbtyXUZnelqISbQnHphDoTH
RMIxMKclpWSvQHkzRhdAehBVaKYaXRPMpGaeRxvTRVFfewirvIDoGvYTAvKSoMFCLUNVFVKrYMeYtBrS
KgiBOjvliNOHLrmztypGhQjtpEQwzVfpVqsTUPvOCPzgqOuvLXJBQZHLmSwGTxEMgCAbogXombCiBDNX
BvGtXjrGWbWHtNCoRuqIZPhBQXZiNUhbmzOiyByAoMSBvusppiPVibIqmLXwXEVfcEAyNeUxaEZThULu
mkGmoLrpOEktwRluXvOmmfEWxZkxUNIqZKuzbaUmLKBYrXMmdOYLEzljzbSJnqRbSiAFyUNyyieKITkh
mvkKyosXKCaTsXQIKczJmxuqIEKeGGGwZyWTolQynlWngjDzFMlwhJFEmODeycbEfxgSRbIXySfwlhZZ
BUBhKyGBHRzWGRXAzarcmSDORvaOMOqYlcVIMwlHGtrLMhFWioqeKfvsJdTXmfQzavzSzCRrVzLFMaBT
DMOPFJcjzXcPvBkzacRmVKTQAvVobGRBypFHvoUdjvBhwWXVdDjvfJOocyIHbMqZGMaRaaFFnmtvTSkY
nIHbmPAtuEszMDFURBYxcOJXKMvJbfSbhiaacxhxiZBnoHTcFeqXQfjTqpcMKFpvvzkpSxlDxSlhikFZ
XSplcknpxiZfwUwGsrfpBUkevEiwndkKrVpWKufWpLTWXcyyXehOcDfnzgTAkhwOAcaiHqJWzsuAvMyD
pDJgeCdAJMwatRfcpKQGTkwxHracsYOlZeXoGthHIRfDBYzhuGEQRKFRnqSEbWDCJObWSAoSwFzVZEnI
rVBwXibUaTwnSTwRmIwkIgoGPRiOMLOTvnzEBBCfcugYZwGSsHRKCJoRsxxzRkKwnTRcRNfbMGssqmXV
IKYzyWHIsCjdzxiHEtvHaufVgcoqVkqIQertevTUTIVMYlNXCGEUzQowqsFpciURKoUwqCRogxeghOWs
cMnuAathgFvNIVqqXpmdJDJPhXQpZCyNbTYktMyTUtQEBeQBhEZzqHotmYREADhFodlcPmTMutBZyefW
sBmsnUbVnHUGAyaDirMoowBwXnzrmfHJgfpAquFoHTuvQvIJcjqiqVdntXbgwpVywbsKxqUMNxYVxBmQ
OAcxOAVPuJeOgABYEHhevhnUOgCUuTBAhJcUGsasbMInGCbHnHXWDdXijDRkUYFuOytTcMPtWklmTHTR
XFTfcFfSSqFUFbQVCKEjUOLveXtsHrIfkphXyDkRELnaTfuaZUClLqbdpWAREJHJpycYRDjElqlVeNya
kTCjDpvFrdnlXogrDZdQzAYaePDdfvHWdcaQGgrrHKBdMnMYbsikbkffVsITSUhEapmLGQYbHoiKGRcg
GPLeEvmCOAkGIuDBdnYPlzuUmLOfetGXpbTbPjjWCZiOJxlDazSbEPVpnNLDsLiwlgleiCdPezQwnNWT
ECLuRGpfJZlnZtcghLucmvlOZNwXaikbKGmoGZJIcsfNnmaHIcPXiEYDHjLKpVtNsqemAmaiTIzvLqlU
mlcvraikZozZwBoExUkELoiaAbTAkqDhrARHQyAvWvYUjthfWjZqbQNTnkgmySsORxGcxouYcyCSkjmC
fpTGOlFoXWLINurMZdQURRnZCiZqsEKeVVZdFMnaoUepdAdARtUuXTvkGzmpEVNZiYSWJAwkcSKgAWTD
mUNVxVebIiavuOAxWUBkuUkXCYtRoZhVNwCZGlaANNpBvXgSDeLURUdQnQteKAXbGlOLGYYYCzCGjzua
UmrdPYuRrUBvLFfwBGTiABTmpANdPCptqKwWXARMKrtmbggOBDgNkeHzNUCIXUIuOAavRbLTnzNNRgzL
boTJooLJIdVFbbjWNngnzPznJglCLEWqulqzSuAyvqYdivDqxEtYPKTwVheFmDidEOnLqjPHBcjoOVvt
MCDmQfwNxkOPuxiJqLQOPRAGJappmpikgmrvRAlKjFjTlaznQldBJmzSMDvCWghWOgfhfkHFZBNdbmMf
MsaQHrtJQvZuGFCrPVBNSNZBFZRdpmQNZYZXpkGjXRAXhELlxDfGhiXwgAUujQbqUCiKaRIYruNDRDlL
zInUkJBpySRZoqwQlqmoxADBjjtGjFPLTkcexYGwGYlANZQaXNgKkPXUUqlViVzxPxxtMQPqOxTcChCg
dvKNliVwzRfMmSsBFeuePnbmVqvyfdOXnZpUopEqfCMnnXpfZnNYwNKiZFPUWWmNCMibsyQEhiodVjTz
UxsicVsZNMXyvBLrdJxGGeCPEutNCzYBRamXwRlmVdqUTPnUoAWaVDshgTHZhvhVlLZsoqbyqOjJMPac
hHqiCKhgFkDUhUDSwsrEwaBrKhXINTjYmHvsTyFdRHliydbfQtRFZcsSTfcSfqyIgQuXLZnrdAwylBmW
BRbmVwdoNFcnoxMKHaYOhgihIsKitcrgEkfjIOKsDPOadFhMwVSKWeCfxxxfWjgNiGDaiYDtMhCgedOR
nTYoeVrpGsyDIsuKhffqaEqoqfWukaQlcUShYicuZAdoYVGvRchUgcmNwxQGogDvKhyAkIuqHCIXQfXp
CtkSSTXTugolUKfqSzugIOpyHhIlcTjDBTKPqcyaRhmgFdSBkYurnvnukNGVoxpZBFmwIEmehuaUcoeu
btkjJqKcAAqxgrKcoRGuqHVUHqKgEaqRCIXlaTqaUewJBEWnTnTJIDYdLeGUMDfndHPYTAGQbhxreADo
WZtdvbJVnNGRNvlAsqIPlpXSXEZGBdqVyNCCwylcXprVoGqnPXZioKnqbdrYlDhbsTVDJqRQKoPtQXzu
RnrGgCfYfeRRxiihjItxHurPwtYJoObDzlEABeIRxQocvWrJtyWchmZXJdYvTgicUircdiMKYAkNbdKu
gPpzXnTQIZxtIhvfBfjIHRaDXbYExxYBvrejpEaVHlinHlYRrhsbChnAwTKlQtHntqcqiXZwTUEdlsVy
WFdZNRfqzkhWzeKMGmkuKoSkuSZRkddsuBNFVMFLPeUkLwCCDKagNjMZwtHcVcEEKyjAYubHipuqNjaV
JukystpMZrhBgLqRVMpaIPsyAvYIsBDVqKNCMLqLwyhJhuWDdCPBgSzJTLkJvaGPirOFwfuMtkyXeKoZ
rGPRJqXyhdYNOXVSqGvbSPozAbjhpyfgGVuNUYaRQomzrTtzAMJnYnyvDnuBkbVvmYzhlhqmwgCZaGJG
GGRbaFdfnDlUfCfhpDWTkWfpUDuUksJvRFNxVYBKGoxBCdhmYZwyDPzWihcQXgByRbYxWZslVsbuTHTf
vaulICCTRkkiYuYoqFdzuxsqOBkzEJHbNXhSnHYxyeGoEklCeaUVEtjxmXyOEzcpsAhfKCTejxOxwGYh
eLtoPpPINviTCHUsgzSkycIxtvekMaoZkBIyLboyvMxxaqfviBxkSALNjiNYqGTypcZDvHonaVBZCSLp
SjRTsJmDuPwKnYwCdTprFvbXnrhARNToXpryIfEoIwSWIdfSKeOHDYwgyUvwXXpKUKQEiyZxCsTkAjME
hdxShAAUYJTkprXuFITxxJuKMiphRAyAeUFZgknMMLvUaSjiMlGmLARvTMpllxEQyfvEqkcONHVFcaTW
tqcbVrgeTLTGuJsrjZdYrrjtoLKcEfjkIhjzXgEkYhZggujFJuQlVtSqvuejtxAEqjgXrYjmwLkSRmXp
pkTfONxRyAxRYqJccLxuhabwMTWfwLTlzuVGJtVJOXxwKjFIZENpGHwRvTRitDBQBesRYATKhmWmmmbP
EXOzdBHNeghlqpjJFmzXyADNHQNEThWDyMsGsTmyFnywIPvDSIcxHbKQHgmJEcfsPzYvSYIbQjnTAgzF
UfZAbwfgCMRxtmZQQyayJFFhCSVeeUcQzSLWqhENNUpyLZaJsQsFQsPyFIjGtcmoJaFQGKTFtKUBdBBo
xECKHgYSMcBWnzRvPyihfjwyjhTTavfYqOrbrgZDSrwVYFjNsdxLJIigfMgythUoUIVSydOnfhAaesXZ
kfyDztQiBCMHjfEGLFllxfejLJjanZVRENsXhIxSWDgbvHHOAFtHzqdfquGbdQvOFlhDiWpxwEolxbep
fVfpKYGMNIQuOlmtTkNRDFTVMtVkEXYUDZKfEihbxXsSLGDcKSHSMXZxAturZVEQgismVAgMVVatqjBM
rXeHaGdccPJMlqhVAePDyEoIRTLCwJpkNTuOjEKEvXaAGhWmhWPHCBMVPkcPklbGIvzMzOFplRUsvZbE
vScmmoKktOUVOeKBcqVvoSsplqqssDvLiPqucbrxoNkodsbrZnvoDfyNGyUAURseEuJPUWsEiVCNcUNd
sxzoRVpEFuFloqWLumNVJITKXnWnOlGpCaQgTLJYizixXoxAHHbodRtPHBbnSzZRZOmlWKOQqvHWAhDh
cYBGRQsFwyesMILhiwjnvjeMIZnHYHYNrmOahjrVPuRgsxdfgUbKCZAVfcOizDeQLKiFQmQQUlDHnCQe
lMnlLSrtXhmGDqISCgElUrZXbXjGGkdWadBbxzVojGQwyhAbWMhSKFFwoIqJfIDdZjUdfCYFkpDdIuWe
aFIUFhnlsREthBRoaquSzBVVOPABfuAYZpoalZwNfZMPOptcoQYVUdRYlXuYChPAdRJgFgwPyTszSXIe
qHRtMxyNlPGoBfpjxHnNvwIADmJmquLgMQGtpJAyvflZjFwAgIymerCTnVkjvqPKFVRscOqAhqvCqCjw
BBojzXKIdphOVTFKhBpnIWYRfuqvQZgVMaqNBkYKzqGaEnBFKZukSLdPbXNmcZtMeykLwlLbZqaHayOb
IWZvbxEXXnaozCHeyiYMnWqIAwJxhMIPDsgySMKhdBYmdrGdbJOfJralshwvhWlmatTsylewdimJEzph
tuTzSGOkGDPPvltRVJPdHRPBTAsKWncfjjuHdlEVOeZIvVnUFHmyGTFDlMGVyAIdzLocbTXIHYTopIok
UHFAVjEXPlsMoKTriyGnfeTlVzvGhVZzUAWWPdZNdIxKioQylFMJZmSToyRGsDJKJXQxPkINvmoHCVUc
RIjImkWWxTnDLQiXdmHqQrWBuvguUUubGByTRnJfkNWxsSupcfIVgboDWzqYHEfAnIKCfdYUOslfXPax
YnaJfNLqJgcxRjBmRpOYgNpZOpzMOCVIRiiXdIqqFxPJhQqJadKiCesOsZoWGWbbQSVRZUlbNZdzeUTE
nhdMSCKCPbpWZguZHGkLiWCisjqnaLbJpbRFAHPjGbHOXKZQXoQQZohmVqjTcdWNhXEjPlLKnjpwbMPQ
ybzDvGgkybXtbDmjQuyOrMrcYGRGGfuuPXzieaetSBidnSRPsLaXKGcxDkXmHbqMWZJXsQkwtojlxOeU
KSIFdVvNEnOUmIZDdlnwtJcPBlcpRWNTazpzgItwJotSLWZruzrMlSGASMWDwOqTpeYYHaTHCCurPdwB
AWzUtwblZXNrBYdjUoDacvmRVURqOzUPlnFISsZMFPtthnDHSsFgkYfsMtXFuNPhLTleWVrmelyFaemo
bVIhEAxNwOUDQCOCDIBHsQlFxCbHErKiBsvQNjuIGnIzZiwoVTdUZnucSaKdHrxJeGQfTawFJefGJFFa
GHzELfnGBmkZyorbbDDwhvEVeIYIGLPMEuZduqFjbeWbVfzVIRZNXwPLgcYUsevuhEQXfYcJshYnJaWz
iqvlswEBRKNYEJidlzdWnQJpBtyjHYVpkQGzdYkeREqjhmmnUIbGZVnwwaMKqgXfURSICNxdteUSGhGZ
UEEFhWRoTKGRwFmPpZPOsalsrNOlkTdXqGKoWlWkqJvYYrtLiTfhdItMbbhdumSYgCcQVUARnYFWkCsC
jElZxrQHIlbTHFLOnrutlvyxzaSIdkJgeyMUnUmtXfnaIedbAInAuQssOQqBTLbvFRiqKqUSdUEmcRmN
LvAxlgliymfbjTwDSqNTLcAEIerzpUShNKkuehciEAYeGJOFFcOvurJFUyfZhQqzfaneiBcrPhaphSCB
StQiJvtoPhHcLUbriDUIfifVFnNtJfGlmcbQJSXsZfVjpbqnkMllUmHzLvEuSarSlNlNHsWvYlfhjMEA
epYTjoRGZeAAtURFeDfDxTYmOmONuQQBdcdncFGjhHmKlwqmUWoXuIXIxaaXnNThgPGtIlynrUIPLQTG
xXhattDrfBGbZRveKbgjzxJLdYREQlMeLtcIEUoyJocdAfUbymxuFLVjGkOQniiPParqoyQYfDYAQTkM
WLicLxpEFkBbwlKrTyYilKTtYkpVGxtOjYmcBDOrwFhFiGutmpTyTarUbVUeSevBTdaPDpjRkaEmLJMg
WsMhSGfIcBChcqrRKgKpjvGnFipjswgjetRtniMagakbCXAjpzWTtMlgZGCJwGyglpcLebrKWhgwJfWV
qGifWNEpCtjuejHoyVCdIxzMYGnfoslgTNAJdtVBWDVoGLzHSAVBTnhNIvAOExQNiJOIPPiHkdaRbfaP
ixDDoCDOOeAqvQJFxLWDICfGmufyxmaMshbvcrtjqqVtffZTnbtCOQfzRMGwOQEKaAmSWjnYdNgvdkmd
dQmaKZSdqKNrnvJlcyVMKuNWmuoOeyKecgjXbmSqnpjwJEaDYoehEklEgJyiksGxdEKgfYRXQecRZgfe
qKWGc
"""

countA = 0  # 统计前边的大写字母
countB = 0  # 统计小写字母
countC = 0  # 统计后边的大写字母
length = len(str1)

for i in range(length):
    if str1[i] == '\n':
        continue

    """
    |如果str1[i]是大写字母：
    |-- 如果已经出现小写字母：
    |-- -- 统计后边的大写字母
    |-- 如果未出现小写字母：
    |-- -- 清空后边大写字母的统计
    |-- -- 统计前边的大写字母
    """
    if str1[i].isupper():
        if countB:
            countC += 1
        else:
            countC = 0
            countA += 1

    """
    |如果str1[i]是小写字母：
    |-- 如果小写字母前边不是三个大写字母（不符合条件）：
    |-- -- 清空所有记录，重新统计
    |-- 如果小写字母前边是三个大写字母（符合条件）：
    |-- -- 如果已经存在小写字母：
    |-- -- -- 清空所有记录，重新统计（出现两个小写字母）
    |-- -- 如果该小写字母是唯一的：
    |-- -- -- countB记录出现小写字母，准备开始统计countC
    """
    if str1[i].islower():
        if countA != 3:
            countA = 0
            countB = 0
            countC = 0
        else: 
            if countB:
                countA = 0
                countB = 0
                countC = 0
            else:
                countB = 1
                countC = 0
                target = i

    """
    |如果前边和后边都是三个大写字母：
    |-- 如果后边第四个字母也是大写字母（不符合条件）：
    |-- -- 清空记录B和C，重新统计
    |-- 如果后边仅有三个大写字母（符合所有条件）：
    |-- -- 打印结果，并清空所有记录，进入下一轮统计
    """
    if countA == 3 and countC == 3:
        if i+1 != length and str1[i+1].isupper():
            countB = 0
            countC = 0
        else:
            print(str1[target], end='')
            countA = 3
            countB = 0
            countC = 0



"""
len_str = len(temp)
secret = ""
for each in range(3, len_str - 3, 1):
    if(temp[each].islower()):
        if(temp[each - 3 : each].isupper() and temp[each + 1 : each + 4].isupper()):
            secret += temp[each]
"""
