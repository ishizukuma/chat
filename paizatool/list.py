#スライス：[開始:終了:間隔]
slice = [0,1,2,3,4]

lst = [1,1,2,2,2,3,3,3,3,1,1,1,1]
#リストの要素で最も多い物を取得（文字でも数字でも可）
maxstr = max(set(lst), key = lst.count)
print(maxstr)
#リストの要素で最も少ない物を取得（文字でも数字でも可）
minstr = min(set(lst), key = lst.count)
print(minstr)

#重複を排除して要素の数を数える
count = len(set(lst))
print(count)

#[]や""を除いてリストを表示
s = ["a","b","c","d","e"]
s = ' '.join(list(s))
print(s)
#さらにそれを逆順にする
s = ''.join(list(reversed(s)))
print(s)
#int型で[]や""を除いてリストを表示、str型を混ぜることも可
num = [1, 2, 3, 4, 5, 10, 100, 555]
n = map(str,num)
print(" ".join(n))

#2次元リストを1次元リストに変換、空のリストも排除される
cards = [[1,2,3],[4,5],[6,7,8,9],[],[]]
cards = sum(cards, [])
print(cards)