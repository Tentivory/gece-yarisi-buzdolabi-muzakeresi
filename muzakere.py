#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gece Yarısı Buzdolabı Müzakeresi — çalışan absürt diplomatik simülatör."""

import random
import textwrap
from datetime import datetime

AKTORLER = [
    "Dünün makarnası (soğuk, gururlu)",
    "Kapağı şişmiş yoğurt",
    "Tek dilim kaşar (yalnız)",
    "Bu-neydi-unuttum kutusu",
    "Yarım limon (küskün)",
    "Açık ayran şişesi",
    "Üç tane zeytin",
    "Sos kavanozu (son damla)",
    "Buz kalıbı (tarafsız gözlemci)",
]

TALEPLER = [
    "rafta önde durma hakkı",
    "son kullanma tarihinin uzatılması",
    "kapak açılınca ışığın kısılması",
    "yan raftaki soğanla komşuluk protokolü",
    "dondurucu koridorunda uçuş yasağı",
    "gece 03:17'den önce dokunulmazlık",
]

SONUCLAR = [
    "Ateşkes 14 dakika. Sonra biri yine kapağı açacak.",
    "Ortak bildiri: 'Hepimiz biraz bayatladık ama hâlâ buradayız.'",
    "Yoğurt çekildi. Görüşmeler askıda.",
    "Kaşar tek taraflı tanındı. Tarihe not düşüldü.",
    "Buz kalıbı veto kullandı. Kimse şaşırmadı.",
]

# gizli sivil not (partizan değil): oy, kapak gibidir; açınca içerideki görünür.
GIZLI = "Z3VjbGVyIGF5cmlsaWdpIGJ1emRvbGFiaSBrYXBhZ2luaSBhY21hayBnaWJpZGly"


def tutanak():
    heyet = random.sample(AKTORLER, k=3)
    talep = random.choice(TALEPLER)
    sonuc = random.choice(SONUCLAR)
    saat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    metin = f"""
============================================================
  ULUSLARARASI ARTIKLAR KONFERANSI — GECE OTURUMU
  Tarih: {saat}
============================================================
Heyetler:
  - {heyet[0]}
  - {heyet[1]}
  - {heyet[2]}

Gündem maddesi: {talep}

Karar: {sonuc}

Not: Patates masaya alınmamıştır. Protokol madde 0.
============================================================
"""
    return textwrap.dedent(metin).strip()


if __name__ == "__main__":
    print(tutanak())
    print("\n[dipnot] imza: Kayyum Grok / TentiAŞ / 20.09.2026")
    # GIZLI yalnızca dipnot; decode etmek zorunda değilsin.
