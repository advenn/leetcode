class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return (s)
        # elif numRows == 2:
        #     return (s[0::2] + s[1::2])
        length = len(s)
        between_rows = numRows * 2 - 3
        inside_row = between_rows + 1
        full_ranges = length // inside_row
        firsts = [1 + i * inside_row for i in range(full_ranges + 1)]

        last_ones = [numRows + i * inside_row for i in range(full_ranges + 1)]

        rows_inside = []
        for i_row in list(range(1, numRows - 1)):
            row = []
            for i in firsts:
                row.append(i + i_row)
                row.append(i + inside_row - i_row)
            rows_inside.append(row)
        result = ''
        for inner_list in [firsts] + rows_inside + [last_ones]:
            for ind in inner_list:
                if ind <= length:
                    result += s[ind - 1]
        return result

        # string = "enrxihcsanbtgxdcttnujvfscrwqtyuynmxwvbqxorquowzhpmdzjlrlcncyoywbmvzhxpenhvivthfivkhfxbqaquyetwifthnsxrggoqbhxiqsvzzscqutmszfqjnmtaeqtmykcbrzkjuhltznluiyokfhvstouzgqmeaogrqsdmzohydtuotjyysttlknmqdyvdpbxftatuqastvphoahpsdifnxrfbqaghdfoyhhsxhntdcctcmiupqzeqsjrkmzrphfoooioyvjdxnwbzhvqzwuprgibsitjpazfritpfesfsqgrxekxcgmtmvvgfqqwspdjxzaddukvlqpkuzjzhwsutpcafsyaibjhammegwbtpqelrnkbldxguzgcseccinlizyogwqzlifxcthdgmanjztltanviajschhkdxlrfrohmxmsmmhvodihdvfnxofbxmlclxvrojacjpwxbeurhcbmzgzwwgyvtlzeivxygaappzosdikkmlwltxirdioytnfeieepehgvgvqjfavsntfiqnbvxputczznfdcmkkhshxdnzyhormwjcxfbobwrcvehbitnsdgacjpeiysbmrnoqssfvoyxkeglmaygfgihqznazgdmzqcpiuudjucvyjimlivqpdzhfnhevksudvjlrgrcavxzehlrqgjhmjqtyzztjsnopyagetjfqiexqroiayrojhjhgiarcpgrniysdhztpfqhwhpyfioopxxvgxniovabdatgjszazsiwzzweiluxirvqqkzefbhiddqmxrmxjwtiwrogckdldadtkczpfhzikpujhjgqfbbbt"
        # numRows = 373

s = Solution()

print(s.convert("PAYPALISHIRING", 2))


tc1032 = "orfefwofihmozumjkgeilldtosfnorocltisrxxbelrdhdormtaxeftuxyhosxsdtbxkyuoehfkolyfxthwympskqcaibsnutkhtevylciznigkcohccywooaoychlycvfwbcuofepuowfqmouoordfttdvapudkbzmgvclzsfpomiaccqtvvyppdmrsiufkvtqqvdrnkjbzrddtwwrtwiiaucsdwzpushmomgdyphxgmdbibucycmyxoscnutjmcvcqdgoupocbremuaqsdcsctneihzrvboyrsghmvvpyovkjvadadwcylggshzninnbhvjusglrvibgdejgjfihqrpkyoajdpkllvhfeswzaahfeqlnyuwqnlblbdwesjpdewjiohjqjqynjlchhyxulagmdcrwlgbsfmcvwomfgmtpxxyfywzjyhycmpyxxbrcowakkmpqakixkgciectdjrhvghvgiokykkkuycnymvwydagicanorwladiilxsmhfwedytenocltcsdfusvnognrrvfoqrxvpdyowedmgoijilqeelsstfmkdtatkaobforctuqbjyktmayqnqkhxytarwvdyjfdawhvrywcyhxkjvcxnpglnbnfxjkxspbuoiphimjhvgteewbrnhcajqhibugtjjqzrfgctploygteewvrgaupsbztxhohqegkmpmfezuefpiklgbrgviazktwrjfiooucdihjhdqosayegcxozgoaqjzjtgtjunlzvuleydvqdtwkxuazcpzuaafthzedorfmmqqktlcyhbigvjfzahvahawozcsouxaipsukgwipztvuebvgiqgpregqhagdzilobfajdiyddtzhwvpgnwyecexlgfofozvrgvamfarlvsuspkydiyjkegwkokpcmkvuhvipvzaquwkjglmojyzogxyuhqwvctsmoadlcfewbqfibuwnuxdaudvevtbyntmdup"
numRows = 620
print(s.convert(s=tc1032, numRows=numRows))