# **Követelméy specifikáció**

## 1. Áttekintés

- Manapság a képek szerepe rendkívül fontos, hiszen minden emlékünket megörökítjük, hogy azt majd később vissza tudjuk nézni.
  - Ezzel az a probléma, hogy nem mindenki rendelkezik drága felszereléssel, kamerával, nem is tanult fényképésznek és még sorolhatnám. Ebből kifolyólag, nem minden kép lesz olyan jó minőségű, mint amilyet szeretnénk.
- A fentebb is említett okból kifolyólag, a felhasználók képszerkesztő programokat szoktak használni, csak az a baj, hogy a legtöbb nagyon bonyolult felhasználói felülettel rendelkezik, az árukról nem is beszélve.
- Itt jönne képbe a mi alkalmazásunk, ami nem csak ingyenes lesz, hanem letisztult felülettel fog rendelkezni, illetve egyszerűen használható akárki számára.
- Az alkalmazás célja, hogy megkönnyítse a képek feljavítását, azok manipulálását és feldolgozását
- Lehetőség lenne a fénykép megtekintésére, feltöltésére.
  - Utóbbinál a felhasználó megváltoztathatja annak kontrasztját, világosságát stb.
  - Lehet majd zöld színű hátteret eltávolítani
  - Szöveget kinyerni egy adott képből, azt pedig opcionálisan átalakítani különböző dokumentumokba (pdf, doc, txt stb.)

---

## 2. Jelenlegi helyzet leírása

- Az iparban a legtöbb szoftver beszerzése, amely képes képek szerkesztésére, és azokra amik fentebb le lettek írva, nagyon költséges, amit nem minden, sőt, a mai árakat figyelembe véve, nem mindenki tud megengedni magának.
- Itt jönne képbe az alkalmazásunk, ami ingyenes lenne, és egyelen webes alkalmazásba foglalná az összes fent említett funkcionalitást.
- Egy piaci rés betöltésére ad lehetőséget az alkalmazás, hiszen ez nem egy bonyolultan kezelhető sok ezer dolláros szoftver lenne amit telepíteni kell, hanem egy ingyenes, könnyen használható weboldal lenne.

---

## 3. Vágyálom rendszer leírása

- Az alkalmazásnak tudni kell futnia a weben, amit bárhonnan el tudnak érni probélma nélkül, ezáltal lehetőséget adva arra, hogy bárhol a világon tudjuk egyből fényképezés után, a képet feltöltve azt szerkeszteni és manipulálni.
- Továbbá mindíg és minden pillanatban elérhető kell hogy legyen, sebességben és reszponzivitásban változatlan, illetve hibamentességét meg kell hogy őrizze.
- Három panelje lenne az alkalmazásnak:
  - Az egyiken az általa feltöltött képét tudná feljavítani
  - A másodikon szöveget tudna kinyerni képekből
  - Végezetül pedig, az utolsó funkcionalitás a zöld hátteres képek hátterének eltávolításáért felelne, amik mögé esetlegesen be lehetne tenni más, szebb képeket, amit csak a felhasználó szeretne.
- A felhasználónak lehetősége lenne az általa módosított, generált dokumentumok letöltésére is.

---

## 4. Funkcionális követelmények

- A felhasználó tudjon képeket feltölteni az oldalra
- A felhasználó fel tudja javítani a képet

  - Tudja a kép kontrasztját javítani
  - Tudja a kép élességét feljavítani
  - Tudja a kép homályosságát állítani
  - Tudja a fényességet csökkenteni
  - Tudja a fényességet növelni
  - Át tudja méretezni a képet

- Ki tudjon nyerni a képből karaktert és azt törölni a képről
- A felhasználó át tudja convertálni a képet: doc, pdf, docx stb. formátummá
- A felhasználó le tudja szedni a hátteret
- A felhasználó hozzátudjon adni hátteret a képhez
- A felhasználó egy felhasználónév megadásával tudjon bejelentkezni
- A felhasználó le tudja menteni a saját preset-jeit
- A felhasználó le tudja menteni az elkészült képet a változtatásokkal
- A weboldal legyen reszponzív
- Tudjon alkalmazkodni különféle képernyő méretekhez

---

## 5. A rendszerre vonatkozó pályázat, törvények, rendeletek, szabványok és ajánlások felsorolása

- A rendszernek/alkalmazásnak a következő megszorításokat kell tartalmaznia
  - Legyen reszponzív a weboldal
  - Innovatív technológiákat kell használnia, ami lehetőleg minden modern böngészőben működik
  - Rendszer/alkalmazás legtöbb böngészőt támogassa
  - A weboldal elérhető legyen a legtöbb böngészőn és operációs rendszeren
  - A felhasználónak a felhasználó nevén kívül mást ne kelljen megadnia
  - A felhasználó a saját preset-jein kívűl mást ne tudjon eltárolni
  - A felhasználók által feltölött képeket tilos elmenteni egy külön tárolóba
  - Tilos trágár, explicit felhasználónevet választani a felhasználónak a bejelentkezésnél
  - Nem szabad, hogy lefagyjon az alkalmazás
  - Tiltott a felhasználó azonosítására alkalmas sütik használata.

---

## 6. Jelenlegi üzleti folyamatok modellje

- Telepített képszerkesztő használata:
  - A legtöbb képszerkesztőt le kell tölteni és telepíteni
  - A legtöbb fizetős és drága
  - A legtöbbet egy ideig lehet használni utána fizetni kell
  - Nem átlátható így a felhasználónak a legtöbb idejét az veszi el hogy az alkalmazás ki kell ismernie
  - Illetve ha a felhasználónak nincs erős gépe akár le is fagyhat az alkalmazás ami az addigi változtatások kárára mehet

---

## 7. Igényelt üzleti folyamatok modellje

- Online elérhető, ingyenes rendszer létrehozása
  - Webes megjelenés mind mobilról (hordozhatóság), mind pedig számítógépről
- Átlátható design kialakítása a weboldalon
  - Photo retouch alkalmazása
  - Contrast állíthatóság
  - Brightness állíthatóság
  - Sharpness állíthatóság
- Letisztult , sima, de elegáns színű háttér
  - Egyszerű betűtípus és betűszín alkalmazása
  - A weboldalon lévő adatok szerkeszthetővé tétele/Könnyű szerkeszthetőség
  - A képet lehet nagyítani, kicsinyíteni
  - Képet lehet letölteni és feltölteni

---

## 8. Követelménylista

| Követelmény azonosító |                                Leírás                                |
| :-------------------: | :------------------------------------------------------------------: |
|          K01          |   Felhasználó/vendég be tudjon lépni a felhasználónevét használva    |
|          K02          |           Telefonon és számitógépen is lehessen használni            |
|          K03          |              Minden internetes keresőn elérhető legyen               |
|          K04          |                          Reszponzív dizájn                           |
|          K05          |                           Dekoratív dizájn                           |
|          K06          |                   Mindig elérhető legyen az oldal                    |
|          K07          |                 Egyszerűen legyen kezelhető az oldal                 |
|          K08          |             Az oldal alkalmazkodjon a kijelző méretéhez              |
|          K09          |          A felhasználó tudjon képeket feltölteni az oldalra          |
|          K10          |                  Tudja a kép kontrasztját javítani                   |
|          K11          |                  Tudja a kép élességét feljavítani                   |
|          K12          |                  Tudja a kép homályosságát javítani                  |
|          K13          |                   Tudja a fényességet csökkenteni                    |
|          K14          |                     Tudja a fényességet növelni                      |
|          K15          |                      Át tudja méretezni a képet                      |
|          K16          |                 Ki tudjon nyerni a képből karaktert                  |
|          K17          | A felhasználó át tudja convertálni a képet: doc pdf stb. formátummá  |
|          K18          |               A felhasználó le tudja szedni a hátteret               |
|          K19          |          A felhasználó hozzá tudjon adni hátteret a képhez           |
|          K20          |          A felhasználó le tudja menteni a saját preset-jeit          |
|          K21          | A felhasználó le tudja menteni az elkészült képet a változtatásokkal |

---

## 9. Fogalomtár
