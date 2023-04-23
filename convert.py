# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1:
#             return s
#         result = ''
#         length = len(s)
#         index = 0
#         while True:
#             result += s[index]
#             index += 2 * numRows - 2
#             if index >= length:
#                 break
#         for row in range(1, numRows - 1):
#             index = row
#             while True:
#                 result += s[index]
#                 index += 2 * numRows - 2 - 2 * row
#                 if index >= length:
#                     break
#                 result += s[index]
#                 index += 2 * row
#                 if index >= length:
#                     break
#         index = numRows - 1
#         while True:
#             result += s[index]
#             index += 2 * numRows - 2
#             if index >= length:
#                 break
#         return result






## the solution below has a big big O notation number
class Solution:
    def convert_invalid(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        numRows -= 1
        indexes = []
        column = 0
        row = 0
        max_column = 0
        # space = ' '
        is_reverse = False
        for index in range(len(s)):
            if row == numRows:
                is_reverse = True
            elif row == 0:
                is_reverse = False
            indexes.append((row, column))
            if is_reverse:
                row -= 1
                column += 1
            else:
                row += 1
            if max_column < column:
                max_column = column
        data = []
        for _ in range(numRows+1):
            data.append("")
        # print("max_column", max_column)
        result = ""
        # print(indexes)

        for row in range(numRows + 1):
            row_data = ""
            for column in range(max_column+1):
                coor = (row, column)
                if coor in indexes:
                    coor_index = indexes.index(coor)
                    row_data += s[coor_index]
                # else:
                #     row_data += space
            result = result + row_data
        # result = "".join(sample_res)
        # result = result.replace("\n","").replace(" ","")
        return result

    def convert(self,  s: str, numRows: int) -> str:
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
# print(s.convert_invalid("PAYPALISHIRING", 3))
# print(s.convert_invalid("PAYPALISHIRING", 4))

print(s.convert_invalid("PAYPALISHIRING", 2) == s.convert("PAYPALISHIRING", 2))
# print(s.convert(string, numRows))

# string = "jclvlazamucimicnewdoxjlfuemdadgkhufsuevjaxrnivcorhfrqqwnujquoyevslqprlyskrhunljgsoxleuyyfqutozqhmgyetyyepfaesjlkzivdevdllygazxjndjrxhrdyyddqnqdoayshwxshxzjywumbffamxdnxjqoyirmirernekxdlicjfqkkvnxuqmszcixmzkwsqoiwyfalpeuuugfrteomqinuqnirxelpstosaodqszkogrfbxtnpdbltqtmpyyeqtujuiokcowswqyxntndxqqsgkhvihbaawjugagloddktdjizynyoesuozryityjrifximkyrokktvusuiqiojfckyatryekijksvusokcyeavwufpctajxkixdbxjmitwcqqxfbbfhbadvfuaaujxfrwkvuuhepdifvfkyhsfiuleafgaapahjwtesplweqfmnmymtqreleinkopmfpvomqueghdmxkynwxzqnswaxgnjwdxbuusgkmnqwqdvadiwahoqakqzqgkmlhqfdimnwzgsplorownpgehioxhhfrvqalwdtksslykajataxgpdmyldxukdnftprrumbmemlrowrhwoqntclghlcrorzhgsbaecplpccdyvnxmdmfhaoplqizkhiqbjtimitdkxiksxjecwmkwabhslievqvwcqeqaztkydwrbgxdcjpalshgepkzhhv"
# numRows = 352
# print(s.convert(string, numRows))
# t317 ="obanbumdladpycygtrgutpdzlajzovccwcqaycfjeibclzkgsqanifmtfxsusuyqzoqxsyjwgkatllbfdesljggpdalxvjnwygvqegpmspgdcjignctxiaonazkxiyvigrbkzqwsfexiogodkjatlqioptlatjkzcllbbhthorpezfhjqkecapqsidubmecoqnsrulakerofyyrpivrkkheumyxzdzpvmhmjvpvbgkhfkyusvneiwjcijajmbzjqiwzfnuhtgoaqmukhjrpfauojwzyxyhnjfooslxorlokzlwjunaanuqzqpzqqifzoupifnwyankayhjsujukgklyckqsswtiskrzxpzackccrlxnwrxecifeuvynrrxlbqkbgkdkufpnsmaqdavhkanfxluperciinlqxoctvrindifjkaqvcgaaruryntivitnhjqcghktnvywfbocfuchoyammwwjerxoapqiwbblwbjdeygksktijuwxqsiwjhklwbtvcwgaaqfeqlqkykthgpgwkostwfhsgapkzw"
# numRows=317

tc1032 = "orfefwofihmozumjkgeilldtosfnorocltisrxxbelrdhdormtaxeftuxyhosxsdtbxkyuoehfkolyfxthwympskqcaibsnutkhtevylciznigkcohccywooaoychlycvfwbcuofepuowfqmouoordfttdvapudkbzmgvclzsfpomiaccqtvvyppdmrsiufkvtqqvdrnkjbzrddtwwrtwiiaucsdwzpushmomgdyphxgmdbibucycmyxoscnutjmcvcqdgoupocbremuaqsdcsctneihzrvboyrsghmvvpyovkjvadadwcylggshzninnbhvjusglrvibgdejgjfihqrpkyoajdpkllvhfeswzaahfeqlnyuwqnlblbdwesjpdewjiohjqjqynjlchhyxulagmdcrwlgbsfmcvwomfgmtpxxyfywzjyhycmpyxxbrcowakkmpqakixkgciectdjrhvghvgiokykkkuycnymvwydagicanorwladiilxsmhfwedytenocltcsdfusvnognrrvfoqrxvpdyowedmgoijilqeelsstfmkdtatkaobforctuqbjyktmayqnqkhxytarwvdyjfdawhvrywcyhxkjvcxnpglnbnfxjkxspbuoiphimjhvgteewbrnhcajqhibugtjjqzrfgctploygteewvrgaupsbztxhohqegkmpmfezuefpiklgbrgviazktwrjfiooucdihjhdqosayegcxozgoaqjzjtgtjunlzvuleydvqdtwkxuazcpzuaafthzedorfmmqqktlcyhbigvjfzahvahawozcsouxaipsukgwipztvuebvgiqgpregqhagdzilobfajdiyddtzhwvpgnwyecexlgfofozvrgvamfarlvsuspkydiyjkegwkokpcmkvuhvipvzaquwkjglmojyzogxyuhqwvctsmoadlcfewbqfibuwnuxdaudvevtbyntmdup"
numRows= 620
print(s.convert(s=tc1032, numRows=numRows) == s.convert_invalid(s=tc1032, numRows=numRows))