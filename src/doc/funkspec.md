# **Funkcionális specifikáció**
## 1. A rendszer céljai és nem céljai
* Az alkalmazásunk célja közé tartoznak a következők:
    * Egyszerű képszerkesztés
    * Innovatív megoldások alkalmazása
    * Dekoratív design
    * Reponzív felület
    * Mindig rendelkezésre álljon
    * Ingyenes legyen
    * Pár kattintás által tudjon szöveget kinyerni egy képből
    * Tudjon minél több formátumba exportálni
    * Hátteret tudjon eltávolítani
* Az alkalmazásunknak nem célja hogy:
    * Más platformokon működjön natív módon
        * Pl. Android, iOS
    * Több nyelvű felhasználói felületet tartalmazzon, hiszen egyszerű és érthető lesz a felület e nélkül is
    * A felhasználó képeit lementse, hiszen az sem etikus, sem biztonságos nem lenne, a GDPR-ra nézve, de ezekről lentebb, a megszorítások résznél lesz bővebb leírás.
    * Professzionális képek előállítása, hiszen ezekre, akik ilyen akarnak ott vannak a nagy gyártók szoftverei.
        * Az alkalmazásunk az egyszerűségre és gyorsaságra törekszik.
---
## 2. Jelenlegi helyzet leírása
* A megrendelő szeretné, ha a képszerkesztés minél gyorsabb, egyszerűbb és innovatívabb lenne.
* A megrendelő szeretné ha mindez ingyenes lenne és egy mindenki számára elérhető weboldalon meg lehetne tekinteni és használni.
    * A weboldal neve legyen egyszerű és jól csengő, hogy mindenki könnyen meg tudja jegyezni.
* Azt szorgalmazza, hogy legyenek külön felületek az egymástól elkülöníthető funkcionalitásokra:
    * Pl. magára a képszerkesztésre egy, a háttér eltávolítására egy illetve külön oldal/fül a szöveg kinyerésére, illetve annak exportálására.
* A felhasználó le tudja tölteni az általa szerkesztett képet.
* A felhasználó le tudja tölteni a konvertált dokumentumot ami az általa feltöltött képből kinyert szöveget tartalmazza.
* Továbbá, az alkalmazás egy piaci rés betöltésére lenne alkalmas
---
## 3. Vágyálom rendszer leírása
* A rendszerünk, mint azt fentebb is említettem három kéepkhez kötődő funkcionalitással fog rendelkezni:
    * A felhasználó fel tudja majd javítani a képeit:
        * Pl. kontraszt, fényesség (brightness), élesség (sharpness) és egyebek változtatása, feljavítása
        * Lenne külön opció *preset<sup>1</sup>*-ek mentésére is, amit később bármikor be tud tölteni, ha beírja az általa kiválasztott felhasználónevet amit az oldal bekér az alkalmazás indulásakor a kezdő képernyőn.
    * El tudja majd távolítani a hátteret a képei mögül, az eltávolítandó szín kiválasztása után, ami mögé majd esetlegesen be tud szúrni/rakni egy másik, általa kiválasztott képet.
    * Ki tudja majd nyerni a szöveget a képeiből:
        * Pl. lefotóz egy számlát, amit dokumentálni szeretne, ezáltal befotózza azt, feltölti az oldalra, az pedig kinyeri belőle a szöveget.
            * Mindezt opcionálisan ki tudja exportálni egy külső formátumba<sup>2</sup> mint például *PDF*, *DOCX*, *DOC* és egyebek.
* A felhasználó le tudja majd menteni az általa szerkesztette, feljavított képet, illetve a kigenerált dokumentumokat.
---
## 4. A rendszerre vonatkozó külső megszorítások: pályázat, törvények, rendeletek, szabványok és ajánlások felsorolása
* A rendszernek/alkalmazásnak a következő megszorításokat kell tartalmaznia:
    * Nem szabad hogy felhasználó adatokat tároljon.
        * Csak a felhasználó által egyedileg kiválasztott felhasználónév tárolására van engedély, ami a későbbi preset-ek beazonosítására fog az alkalmazás használni.
    * Tiltott a felhasználó azonosítására alkalmas sütik használata.
    * Innovatív technológiákat kell használnia, ami lehetőleg minden modern böngészőben működik
    * Nem szabad, hogy lefagyjon az alkalmazás
    * Tilos trágár, explicit felhasználónevet választani a felhasználónak a bejelentkezésnél
    * Tilos tárolnia a felhasználó képeit, hiszen az a GDPR bizonyos szabályaival szembe menne.
---
## 5. Jelenlegi üzleti folyamatok modellje

---
## 6. Igényelt üzleti folyamatok modellje

---
## 7. Követelménylista

---
## 8. Használati esetek

---
## 9. Megfeleltetés, hogyan fedik le a használati esetek a követelményeket

---
## 10. Képernyő tervek

---
## 11. Forgatókönyvek

---
## 12. Funkció – követelmény megfeleltetés

---
## 13. Fogalomszótár
1. Egy preset, az amikor a felhasználó beállítja a különböző képszerkesztési beállításokat, s azokat lementi, hogy később is be tudja majd tölteni és felhasználni őket.
2. Ezek különböző elektronikus szöveges dokumentum formátumok, a PDF-et hivatalos dokumentumok továbbítására szokták használni, mivel alapvetően nem szerkeszthető. A DOC illetve DOCX pedig a Microsoft Word szöveges dokumentumainak a formátumai. 