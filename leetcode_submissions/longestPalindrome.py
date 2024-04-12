import time

start = time.time()


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Input: s = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.
        ___________
        Input: s = "cbbd"
        Output: "bb"
        ___________
        :param s:
        :return:
        """

        # def isPalindrome(s):
        #     return s == s[::-1]
        def isPalindrome(s: str) -> bool:
            if not s:
                return False
            return s == s[::-1]
            # length = len(s) - 1
            # first = 0
            # mid = length // 2
            # while True:
            #     if s[first] == s[length]:
            #         first += 1
            #         length -= 1
            #     else:
            #         return False
            #     if first > mid:
            #         return True

        if isPalindrome(s):
            return s
        length = len(s)
        first = 0
        longest = ""
        while True:
            string = s[first:length]
            secleng = len(string)
            second = 0
            spider = 2
            while True:
                cut = string[second : second + spider]
                if not cut:
                    spider += 1
                    continue
                # print(cut, longest)
                if isPalindrome(cut) and len(longest) < len(cut):
                    longest = cut
                spider += 1
                if spider > secleng:
                    break
            first += 1
            if first >= length:
                return longest


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return None
        if len(s) == 1:
            return s

        P = [[False] * len(s) for i in range(len(s))]

        for i in range(len(s)):
            P[i][i] = True

        for i in range(len(s) - 1):
            P[i][i + 1] = s[i] == s[i + 1]

        for s_len in range(3, len(s) + 1):
            for i in range(len(s) + 1 - s_len):
                P[i][i + s_len - 1] = P[i + 1][i + s_len - 2] and (
                    s[i] == s[i + s_len - 1]
                )

        ip = 0
        jp = 0
        max_len = 1

        for i in range(len(s)):
            for j in range(len(s)):
                if P[i][j] and j + 1 - i > max_len:
                    max_len = j + 1 - i
                    ip = i
                    jp = j
                    continue

        return s[ip : jp + 1]


s = Solution()
# print(s.longestPalindrome("pcagacp"))
print(
    s.longestPalindrome(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    )
)
# print(time.time() - start)
print(
    s.longestPalindrome(
        "pihoigwlvzvtrugdolvtzrkyelaqdvbijzmkhebzawboaxkdjyfocpewwztffuaibcqurwwmijmvrnpfcoglyxpxkrbhupoxcafabxtoecodsjgngrionuvzaiigevuvruxxiwpjzjlqgenglhprcgzgpdzabrjhkbtfrbmwpcszepxhwiwdhvnpsmhhaiqsbeiwsaeomqtzcpjzfknejxlxwtpkufanhuoyjgihdzhtxnyctazzvnttjspfztjurdwmmzrvobcatkorfhpieoqfetcglembkgbexsznuduhrfoxkbswkanqwfkoktnnujqetijaqhrxuhkgsezfdrncbaltctwcourdbpdwhqlsxfwsoaduaqkbjeekwwykptjthhtokrvzsuelsywyznqscnwiszogzqvfsgggzltlvzkllinpfaigswquqfvabbzvestwxhbnfjhnvfhyxalchmtkcwnyyrbwjsoqooypwteozbivqiyldpqlykxinmzkgnmfbobgjivlzubfen"
    )
)
# print(isPalindrome("aavttvaa"))
print(
    s.longestPalindrome(
        "wsgdzojcrxtfqcfkhhcuxxnbwtxzkkeunmpdsqfvgfjhusholnwrhmzexhfqppatkexuzdllrbaxygmovqwfvmmbvuuctcwxhrmepxmnxlxdkyzfsqypuroxdczuilbjypnirljxfgpuhhgusflhalorkcvqfknnkqyprxlwmakqszsdqnfovptsgbppvejvukbxaybccxzeqcjhmnexlaafmycwopxntuisxcitxdbarsicvwrvjmxsapmhbbnuivzhkgcrshokkioagwidhmfzjwwywastecjsolxmhfnmgommkoimiwlgwxxdsxhuwwjhpxxgmeuzhdzmuqhmhnfwwokgvwsznfcoxbferdonrexzanpymxtfojodcfydedlxmxeffhwjeegqnagoqlwwdctbqnuxngrgovrjesrkjrfjawknbrsfywljscfvnjhczhyeoyzrtbkvvfvofykkwoiclgxyaddhpdoztdhcbauaagjmfzkkdqexkczfsztckdlujgqzjyuittnudpldjvsbwbzcsazjpxrwfafievenvuetzcxynnmskoytgznvqdlkhaowjtetveahpjguiowkiuvikwewmgxhgfjuzkgrkqhmxxavbriftadtogmhlatczusxkktcsyrnwjbeshifzbykqibghmmvecwwtwdcscikyzyiqlgwzycptlxiwfaigyhrlgtjocvajcnqyenxrnjgogeqtvkxllxpuoxargzgcsfwavwbnktchwjebvwwhfghqkcjhuhuqwcdsixrkfjxuzvhjxlyoxswdlwfytgbtqbeimzzogzrlovcdpseoafuxfmrhdswwictsctawjanvoafvzqanvhaohgndbsxlzuymvfflyswnkvpsvqezekeidadatsymbvgwobdrixisknqpehddjrsntkqpsfxictqbnedjmsveurvrtvpvzbengdijkfcogpcrvwyf"
    )
)
# def isPalindrome(s: str) -> bool:
print(
    s.longestPalindrome(
        "okfzopfdxngrcukpqwmgyfbwzkqegoglsqszdihswhcnwaajuiagxscrwoicsdvyowbowaddignjgsjrhhhookusgnykutrkpogmvruwdkpjucslsoluhnooysjichvobriksbanovvynfwtooygdtflnchtgcycjiziytrhsomevozdxxbiwiuxrhxtyefogphgavlhbvdjpcosexyrmphcyuhqymnzkngqyitzekwimveydjrxkhvhckqcjetpmhxzisdlkhmotwcgejllzdmfwrbpzuxcawgamamkziewwqnxpvyhvmzulivwrngrsnarsmeunbpbnnvvlxllvniskaerpawflwfdozfsmovvjtymsgnvmfepidyffwjxpvpgwceukgfplqcyccejatqqmefquirgztnyawkruasuitnjldxgmmqzzvwltetjyenbicgabtnkpfdcanggcensptcgyyygnkbvcgmvzichisofakajqtsfogqewegawcjtylxavxdxdznzyxyvvupnwfxogyjmbayeminbzthyidymnmuoevrgfbdpodbdrznmosuispnmimrglgrkdrdsjmyacfmuntvgpjaginmyknawgonibhifpyhqoswyefidrtsqgwqviseayzxqwgelgtnvxlrdhpnuhxhianiqjiyygagwwmyklszbyhcykhejijhnfmrsagsbfthmzmzractm"
    )
)

#     length = len(s) - 1
#     first = 0
#     mid = length // 2
#     while True:
#         if s[first] == s[length]:
#             first += 1
#             length -= 1
#         else:
#             return False
#         if first > mid:
#             return True
# def isPalindrome( x: int) -> bool:
#     temp = x
#     reverse = 0
#     while x > 0:
#         digit = x % 10
#         reverse = reverse * 10 + digit
#         x = x // 10
#     if temp == reverse:
#         return True
#     return False

print(time.time() - start)

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
