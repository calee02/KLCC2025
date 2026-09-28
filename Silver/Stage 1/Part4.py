# 📌 Part 4 – Decrypt Rotating Shift Cipher

"""
1. Task:
- Decrypt a secret message encoded with a repeating list of integer shift keys 
- Shift letters backward along the alphabet (A=0 ... Z=25)
- Spaces remain unchanged

2. Rule:
- Cycle the Keys: Loop through each character
- If it's a space, keep it as a space
- If it's a letter, subtract the key at index key_index % len(keys) and wrap around using % 26
- Move to the next key for the next letter
"""

def decrypt_rotating_cipher(ciphertext, keys):
    decrypted = []
    key_idx = 0
    num_keys = len(keys)
    
    for ch in ciphertext:
        if 'A' <= ch <= 'Z':
            shift = keys[key_idx % num_keys]
            # Convert 'A'-'Z' to 0-25
            orig_pos = ord(ch) - ord('A')
            new_pos = (orig_pos - shift) % 26
            decrypted.append(chr(ord('A') + new_pos))
            key_idx += 1
        else:
            decrypted.append(ch)  # Keep spaces unchanged
            
    return "".join(decrypted)

# Example:
"""
Input:
MESSAGE FROM BUNKER
5 1 9
Output:
HDJNZXZ EIJL SPMBZQ
"""
print(decrypt_rotating_cipher("MESSAGE FROM BUNKER", [5,1,9]))
# Ans: HDJNZXZ EIJL SPMBZQ

# Input 1:
print(decrypt_rotating_cipher("RD XKZ KOTKOVA PMUBK SYB ZZJQXMM LOZQGXLN JBOZQRI NTISBQNIP DMAR RTRX TEFM ZGMKJZTE AQFJ INIQARDJQ JMCV HNMB VS ATRM XOJHU MCD TXNSVOG QFXWRZPP YTV MJ VKXHX AKJMVP", [5,1,9,3,7]))
# ans: MC OHS FNKHHQZ GJNWJ JVU UYANQHL CLSLFOIG EAFWJMH EQBNAHKBK CDXK MSIU MZED WZHJAWMZ ZHCC DMZNTMCAN CHBM EGHA MPTOQD UHEGL JVY SOKLQNX NYSVIWIK XKS FE UBUAS ZBGFQO


# Input 2:
print(decrypt_rotating_cipher("HDCQ ZG U OZGPLCDJ PLYYJAEMQTFB ISC DKMGEZCJ GD AWLIPU XS L PNII BYGV BIMO TKL EYFAY ORMO YYU W PLUWK UTKV FMH PWNRPIM MCGVFWF NYWHXPPE WLC NWPB FJ LFCLJS MCYU W RPRA QGEY IYBTTOH ITKG QYEVF ULO PHULVVHO UP QWHLZK IITP TWL", [12, 4, 6, 2, 15, 9]))
# Ans: VZWO KX I KTEACQZD NWPMFUCXHHBV GDT RGGEPQQF AB LNZEJS IJ Z LHGT SMCP ZTDC PEJ PPTWS MCDC USS H GZQQI FKYR ZKS GKJLNTD AYATQNT JSUSODLY UWT BSJZ QA ZBWJUJ AYSS H IDNU ORVM ESZEKCD CRVX EUYTQ LZK JFFCJRBM FG ESBJKB WENN ENZ

# Input 3: 
print(decrypt_rotating_cipher("RDZTKF WBXI OQJJFDXS FAT THHMUMPI BH OHBMDHBFEXS IX XDX EAESFZZ XZW CDTRQGKTP WD ZHI EXCA TTOUTA ENEMAKI PNT FH EQTI EXTH VD DKXR KUZWQ HEBDTIFAGH BKTCQKGBP LB PXIX UIMZ TUMW M VOQXC REPFD", [3, 14, 7, 11]))
# Ans: OPSIHR PQUU HFGVYSUE YPQ FAWJGFEF NA DENFSENYTUE BM UPQ TXQLUWL QOT OWIOCZZQB PS WTB TUOT IQANIX QGTJMDX MZM UEQJIF QQIE HW SHJK ZRLPF EQUSQUYPDT UZQOJZDNI AY BQXU GBBW FNBT Y ODNJV GBBYS