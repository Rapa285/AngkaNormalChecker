from GeneratePattern import generatePattern as gp
import StringMatcher as sm
import mpmath
import Champernowne as cp

def main():
    
    print("Pilih masukkan angka :")
    print("1). Input Manual")
    print("2). Bilangan Champernowne")
    print("3). Pi")
    txt_opt = int(input("Pilih salah satu opsi (1/2/3) : "))
    text = ""
    match(txt_opt):
        case 1:
            text = str(input("Masukkan angka : "))
        case 2:
            n = int(input("Banyak digit Champernowne : "))
            text = cp.champernowne_constant(n)
        case 3:
            n = int(input("Banyak digit Pi (belakang koma) : "))
            mpmath.mp.dps = n+2  # Decimal places
            pi_value = str(mpmath.mp.pi)
            text = pi_value[2:n+2]
    
    # print(text)
    digit = int(input("Masukkan banyak digit dalam suatu sekuens : ")) # 1 -> 0..9 , 2 -> 00..99, 3 -> 000..999
    pattern = gp(digit)
    freq = [0 for i in range (len(pattern))]
    totaltime = 0
    print("Pilihan Algoritma Pencarian")
    print("1). Brute Force")
    print("2). Knuth Morris Pratt")
    print("3). Boyer-Moore")

    algorithm = int(input("Pilih algoritma (1/2/3) : "))

    for i in range (len(pattern)):
        result,count,time = searchAlgorithm(algorithm,text,pattern[i])
        freq[i] = count
        totaltime += time
        print(f"pattern : {pattern[i]}, freq : {freq[i]} freq(%) : {freq[i]/len(text)*100}%")
    print(f"total number : {len(text)}")
    print(f"total time : {totaltime*1000}ms")
    
    

def searchAlgorithm(algorithm : int, text,pattern):
    match algorithm:
        case 1:
            return sm.bruteforceStringMatcher(text,pattern)
        case 2:
            return sm.kmp_search(text,pattern)
        case 3:
            return sm.boyerMoore(text,pattern)

main()