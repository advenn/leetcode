# leetcode link: https://leetcode.com/problems/nth-digit/description/
class Solution:
    def findNthDigit(self, n: int) -> int:
        """bir dan to'qqizgacha 9 ta belgi
        10 dan 99 gacha 180 ta belgi
        100 dan 999 gacha (999-100 + 1) * 3  =  2.700 ta belgi
        1000 dan 9999 gacha (9.000) * 4 = 36.000 ta belgi
        10000 dan 99999 gacha 90.000 * 5 = 450.000 ta belgi
        100000dan 999999gacha 900.000 * 6 = 5 400 000 ta belgi
        1.000.000 dan 9.999.999 gacha 9.M * 7 = 63M
        10M dan 99M gacha 90M * 8 = 720M
        100M =>  900M * 9 = 8.100.000.000

        sample: 100000 ni topish kk
        1 dan 9 gacha 9 ta qo'shildi,
        10 dan 99 gacha 180 qo'shildi
        100 dan 999 gacha 2700 qo'shildi
        1000dan 9999 gacha 36.000 qo'shildi
        10000 dan 99999gacha 450.000 qo'shildi
        9 + 180 + 2700 + 36k + 450k > 100k dan
        shunda, birinchi yig'indi (450k siz) 38.889 bo'ldi
        sanoq boshi endi 10.000
        100.000 dan 38.889 ni ayiramiz. 100.000 - 38.889 = 61.111
        get_log bilan xonalik raqamlarni olamiz: get_log(10000) => 5
        61.111 ni 5 ga bo'lamiz: 12.222.2
        qoldiqni olamiz: 61.111 % 5 = 1
        agar qoldiq bor bo'lsa:
            butun qismni sanoq boshiga qo'shamiz: 10.000 + 12.222 =>  22.222
            next number ni olamiz 22.222 + 1 = 22.223
            str ing qilamiz = "22223"
            oldiga bitta belgi qo'shamiz:  "." + str(son)
            string ning qoldiqdagi index dagi belgini int qilib qaytaramiz
            return int(str(son)[qoldiq])
        agar qoldiq == 0 bo'lsa
            sonning o'zini olamiz: 22.222
            return int(str(son)[-1])
            qilamiz
        """
        raqamlar_list = {
            1: 9,
            2: 180,
            3: 2700,
            4: 36_000,
            5: 450_000,
            6: 5_400_000,
            7: 63_000_000,
            8: 720_000_000,
            9: 8_100_000_000
        }
        def get_log(num: int):
            count = 0
            while num >= 10:
                num //= 10
                count += 1
            return count + 1
        count = 0
        raqam = 1
        while count < n:
            if (count + raqamlar_list[raqam]) < n:
                count = count + raqamlar_list[raqam]
                raqam += 1
            else:
                break
        sanoq_boshi = 10**(raqam - 1) - 1
        rest = n - count
        qoldiq, number = rest % raqam, rest // raqam
        if qoldiq:
            next_num = sanoq_boshi + number + 1
            num_str = "." + str(next_num)
            return int(num_str[qoldiq])
        else:
            next_num = sanoq_boshi + number
            return int(str(str(next_num)[-1]))












s = Solution()
print(s.findNthDigit(9+2))


# def get_log(num: int):
#     count = 0
#     while num >= 10:
#         num //= 10
#         count += 1
#     return count + 1
#
#
# print(get_log(1))
# print(get_log(10))
# print(get_log(100))
# print(get_log(999))
# print(get_log(1134))
# print(get_log(13413))
# print(get_log(134135))
