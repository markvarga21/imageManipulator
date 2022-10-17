# **Rendszerterv**
## 1. A rendszer célja
---
## 2. Projektterv
---
## 3. Üzleti folyamatok modellje
---
## 4. Követelmények
---
## 5. Funkcionális terv
---
## 6. Fizikai környezet
---
## 7. Absztrakt domain modell
---
## 8. Architekturális terv
---
## 9. Adatbázis terv
* A szavak tárolására NoSQL adatbázis rendszert fog használni a rendszer, azon belül is a Redis-t
* Mivel a Redis lehetőséget ad ingyenes szerver és adatbázis host-ra, ezért a Redis Cloud online szolgáltatását használjuk az adatbázis hostol-ására.
* Az alkalmazás kihelyezése után, nagy eséllyel elő lesz fizetve egy nagyobb plan, ami több tárhelyet ad.
* A webalkalmazás három fő adatszerkezetet (mivel a Redis egy memória-beli kulcs-érték adatbázis) fog tartalmazni:
    * Egy csúnya szavakat tartalmazót, hogy a felhasználó ne használhasson csúnya, tiltott, obszcén szavakat sem felhasználónévként, sem az lementendő kép/dokumentum neveként.
    * Egy felhasználóneveket tartalmazó listát, ami csupán a nevek tárolására hivatott.
    * Minden névhez egy listát, ami a felhasználó által elnevezett és lementett preset-ek nevei tartalmazza.
    * Minden preset-hez egy hash-t, amiben tárolva vannak a kívánt, adott képen alkalmazandó, betöltendő beállítások.
        * Mint például kontraszt (*contrast*), fényesség (*brightness*), élesség (*sharpness*), szín intenzitása (*color*) és homályosság (*blur*)
* Az adatbázis eljárások között szerepelni fog az újonnan regisztrált felhasználók bevitele az adatbázisba, illetve presetek létrehozása és perzisztálása.
    * A fentieken kívül pedig, le lesznek kérve, illetve filterezve is lehetnek az elemek.
* Az adatbázis modelljének diagrammja a következő képpen néz ki:<br>
![Database model](../resources/dabataseModel.png)
---
## 10. Implementációs terv
---
## 11. Tesztterv
---
## 12. Telepítési terv
---
## 13. Karbantartási terv
