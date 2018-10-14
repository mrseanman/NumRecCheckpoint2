from Organise import Organise

def main():
    #does all this
    do = Organise()
    print("#########################################\nFinding linear fit params using CHISQUARE\n#########################################")
    do.findChiParams()
    print("#########################################\nFinding ExpPDF params using MAXLIKELYHOOD\n#########################################")
    print("-----------------------\n1K Data Points\n-----------------------")
    do.findNLLParams("1KMuonData.txt")
    print("-----------------------\n10K Data Points\n-----------------------")
    do.findNLLParams("10KMuonData.txt")

main()
