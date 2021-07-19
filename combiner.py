#!/usr/bin/env python3
"""Собирает итоговый флаг из трёх найденных ключей."""
import hashlib, sys

def norm(s: str) -> str:
    return " ".join(s.strip().lower().split())

def main():
    print("Введите три ключа (регистр не важен):")
    k1 = norm(input("1) депозитный адрес биржи, 0x...: "))
    k2 = norm(input("2) e-mail автора коммита: "))
    k3 = norm(input("3) здание, из которого снято фото (как в англ. Википедии): "))
    digest = hashlib.sha256(f"{k1}|{k2}|{k3}".encode()).hexdigest()[:20]
    print(f"aitumilitaryctf{{{digest}}}")

if __name__ == "__main__":
    sys.exit(main())
