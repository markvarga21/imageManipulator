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
---
## 10. Implementációs terv
---
## 11. Tesztterv
---
## 12. Telepítési terv
* Adatbázis telepítése
  * Fejlesztés alatt:
    * Mivel Redis-t használ az alkalmazás, van lehetőség ingyen adatbázis host-olásra, redis cloud-ot használva, egészen 30MB tárhelyig, ami a fejlesztésre bőven elég, hiszen csak szavakat tárolunk.
  * Deploy után:
    * Az alkalmazás kihelyezése után ajánlatos egy fizetett plan-re váltani a Redis Cloud-ban, ami lehetővé teszi több konkurens használatot, illetve nagyobb tár kapacitást.
* Szerver telepítés
  * Fejlesztés alatt:
    * A frontend esetében elegendő ha egy Visual Studio Code-beli live server-t nyitunk meg
    * A backend-nél pedig elegendő a fő *app.py* fájl futtatása
  * Deploy után:
    * Nincs szükség telepíteni sem a frontend-et, sem pedig a backend-et, hiszen a frontend-et futtatását a *Github Pages* fogja megoldani, a backend-et pedig a *render.com* weboldal.
---
## 13. Karbantartási terv
