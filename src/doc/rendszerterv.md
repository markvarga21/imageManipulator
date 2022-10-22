# **Rendszerterv**
## 1. A rendszer célja
* A rendszer célja, hogy a felhasználó képet tudjon beolvasni, és különböző műveleteket megcsinálni rajta. Pl.:
  * Tudja a kép kontrasztját javítani
  * Tudja a kép élességét feljavítani
  * Tudja a kép homályosságát állítani
  * Tudja a fényességet csökkenteni
  * Tudja a fényességet növelni
  * Át tudja méretezni a képet
  * A felhasználó át tudja convertálni a képet: doc, pdf, docx stb. formátummá 
  * A felhasználó le tudja szedni a hátteret
  * A felhasználó hozzá tudjon adni hátteret a képhez
  * A felhasználó egy felhasználónév megadásával tudjon bejelentkezni
  * A felhasználó le tudja menteni a saját preset-jeit
  * A felhasználó le tudja menteni az elkészült képet a változtatásokkal
  * Internet szolgáltatás nélkül elérhető az oldal. <br>
  * Annak érdekében, hogy átlátható legyen az alkalmazás, a design-ra elég nagy figyelmet szentelünk. <br>
  * A mostanában divatos reszponzív design-t fogjuk használni. <br>
  * A cél egy olyan oldal létrehozása amely bárki számára bármikor rendelkezésre áll a neten.
---
## 2. Projektterv
### Projektszerepkörök, felelősségek:
* Scrum master: Varga József-Márk, Bódi András, Cserés Gábor
* Product owner: Varga József-Márk, Bódi András, Cserés Gábor

### Projektmunkások és felelőségek:

* Backend munkálatok:
    * Varga József-Márk
         * Feladata a funkciók létrehozása illetve a preset-ek elmentése
* Frontend:
    * Bódi András, Cserés Gábor
         * Feladatuk az elkészült képernyőtervek alapján létre hozni a weboldal megjelenését
### Ütemterv:

|          Funkció        |Feladat|Prioritás|Becslés|Aktuális becslés|Eltelt idő|Hátralévő idő|
|          :----:         |:----: |  :----: | :----:|     :----:     |  :----:  |    :----:   |
|Követelmény specifikáció |       |0        |7      |7               |7     |       0     |
|Funkcionális specifikáció|       |0        |7      |7           |7     |   0     |
|       Rendszerterv      |       |0        |7      |7           |7     |   0     |
|         Frontend        |       |2        |-      |-               |0     |   -     |
|         Backend         |       |2        |-      |-           |0     |   -     |

---
## 3. Üzleti folyamatok modellje
* Üzleti szereplők
    * **Felhasználó**: ez alatt értetik bármely felhasználó, akármilyen korcsoportban, aki az alkalmazást használni akarja.
    * **Admin**: akinek jogosultsága van a rendszer karbantartására és szerkesztésére
    * **Tesztelők**: lehetnek akár fejlesztők (az alpha tesztelés esetében), vagy az alkalmazás béta tesztelői, akik véletlenszerűen lettek kiválasztva a felhasználói bázisból.
* Üzleti folyamatok:
    * Fénykép feltöltése a platformra, amit az adott felhasználó szerkeszteni, manipulálni szeretne.
    * Manipulációs mód kiválasztása, legyen az a kép feljavítása, háttér eltávolítása avagy szöveg kinyerése és exportálása az előre megadott kimeneti formátumok egyikébe.
    * Szerkesztett kép vagy dokumentum letöltése.
* Üzleti entitások:
    * Maga a webalkalmazás (mivel maga az alkalmazás csekély méretű)
* Szemléltető folyamatábra:<br>
![Flowchart](../resources/flowChart.png)
---
## 4. Követelmények
* Funkcionális követelmények:
    * Felhasználó/vendég be tudjon lépni a felhasználónevét használva
    * Telefonon és számitógépen is lehessen használni
    * Minden internetes keresőn elérhető legyen
    * Mindig elérhető legyen az oldal
    * Egyszerűen legyen kezelhető az oldal  
    * Az oldal alkalmazkodjon a kijelző méretéhez
    * A felhasználó tudjon képeket feltölteni az oldalra
    * Tudja a kép kontrasztját javítani 
    * Tudja a kép élességét feljavítani 
    * Tudja a kép homályosságát javítani
    * Tudja a fényességet csökkenteni
    * Tudja a fényességet növelni
    * Át tudja méretezni a képet 
    * Ki tudjon nyerni a képből karaktert 
    * A felhasználó át tudja convertálni a képet: doc pdf stb. formátummá
    * A felhasználó le tudja szedni a hátteret  
    * A felhasználó hozzá tudjon adni hátteret a képhez
    * A felhasználó le tudja menteni a saját preset-jeit
    * A felhasználó le tudja menteni az elkészült képet a változtatásokkal

* Nem funkcionális követelmények:
    * A felhasználó ne tárolhasson a felhasználó nevén kívűl más adatát eltárolni, illetve felhasználó ne tárolhasson preset-eken kívűl más adatot
    * Felhasználót ne lehessen azonosítani
    * Nem szabad, hogy lefagyjon az alkalmazás
    * Tilos trágár, explicit felhasználónevet választani a felhasználónak a bejelentkezésnél
    * Ne lehessen tárolni a felhasználó képeit, hiszen az a GDPR bizonyos szabályaival szembe menne.

* Törvényi előírások, szabványok:
    * GDPR-nek való megfelelés.

---
## 5. Funkcionális terv
* A webalkalmazásunknak az a célja, hogy azon embereket segítsük akik nem engedhetik meg maguknak a drága képszerkesztőket illetve ha nincs olyan erős gépük azokhoz. 
* Rendszerszerepkörök:
    * Felhasználó(user)
    * Fejlesztő

* Rendszerhasználati esetek és lefutásaik:
    * Felhasználó(user):
        * Bejelentkezés:
            * 1.: A felhasználó megadja a felhasználónevét
            * 2.: Rá kattint a bejelentkezésre
            * 3.: A rendszer bejelentkezteti azzal a felhasználónévvel
        * Kép feltöltése:
            * 1.: A fő oldalon a felhasználó rá kattint az upload gombra
            * 2.: Majd előkeresi a szerkesztésre váró képet
            * 3.: Ha ez megvan és feltölti akkor a kép megjelenik a fő oldalon
        * Kontraszt javítás: 
            * 1.: A CONSTRAST szöveg alatti vonalon lehet egy pontot mozgatni amivel lehet a kontrasztot állítani
        * Élesség javítás:
            * 1.: A SHARPNESS szöveg alatti vonalon lehet egy pontot mozgatni amivel lehet az élességet állítani
        * Fényesség csökkentése vagy növelése:
            * 1.: A BRIGHTNESS szöveg alatti vonalon lehet egy pontot mozgatni amit ha balra húzunk akkor a fényesség csökken ha jobbra akkor növeljük
        * Homályosság javítása:
            * 1.: A BLUR szöveg alatti vonalon lehet egy pontot mozgatni amivel lehet a homályosságot állítani állítani
        * Katakter kinyerés képből:
            * 1.: A bal oldali sávnál ki kell választani a második ikont
            * 2.: Azon a külön oldalon lehet a szöveget kinyerni a képből
        * Kép átkonvertálása:
            * 1.: A főoldalon a bal oldali sávban ki kell választani a harmadik ikont és ott lehet a képet átkonvertálni doc, pdf, vagy docx formátumú fájlá    
        * Kép letöltése:
            * 1.: A felhasználó elvégzi a szükséges változtatásokat a képpel
            * 2.: Rá kattint a download gombra Aminek következtében a felhasználó le tudja tölteni a képet
    * Fejlesztő:
        * A fejlesztő végre tudja hajtani azokat a dolgokat mint a felhasználó
        * A weboldal kódján tud változtatni és tesztelni
        * Ha szükséges és igény van rá akkor új funkciókat tud hozzáadni a rendszerhez

* Menü hierarchiák:
    * Fő oldal: <br>
![Home page](../resources/homePage.png)

---
## 6. Fizikai környezet
* Az alkalmazás web platformra készül így különféle eszközökön lehet használni ha van rajtuk böngésző és internet kapcsolat
* Operációs rendszer független
* Nincsenek megvásárolt komponenseink
* Van tűzfal a hálózaton és minden portot engedélyez

* Fejlesztési környezet:
    * Visual Studio Code
    * Git
    * Pycharm

---
## 7. Absztrakt domain modell
* Frontend:
    * HTML: A HTML egy leíró nyelv, melyet weboldalak elkészítéséhez találtak fel, és mára <br>
      már internetes szabvánnyá vált.
    * CSS: A CSS egy stílusleíró nyelv, mely a HTML vagy XHTML típusú strukturált dokumentumok<br>
      stílusát írja le. Weblapunk stílusát ezzel szabályozhatjuk.
    * JavaScript: A JavaScript programozási nyelv egy objektumorientált, prototípus-alapú szkriptnyelv, <br>
      amelyet weboldalakon sokat használnak. A weblapunk programozásához fog majd kelleni.

* Backend:
    * A backendhez python flaskot, redist, Pillowot, opencv-t használunk.
---
## 8. Architekturális terv
* A webalkalmazásunkban lesz egy elkülönített frontend illetve egy backend.
    * Az alkalmazás frontend részen a HTML, JavaScript és CSS hármas kombinációját fogja alkalmazni
    * Backend részen a python nyelvbeli *Flask* framework lesz használva a Rest API kiépítésére, illetve további külső szolgáltatásokat, modulokat a funkcionalitások kielégítése végett.
* A frontend tehát HTML-t fog használni az elemek összefűzésére, CSS-t az elemek stilizálására, JavaScript-et az elemek manipulálására és a backend-del való kommunikálásra.
* A backend pedig a Flask keretrendszerre fog épülni, ami fogja még használni továbbá a Redis, openCV, Pillow és egyéb konvertáló python modulokat.
* Utóbbi lehetővé fogja tenni a különböző rétegek szétválasztását (model, nézet, vezérlő - MVC architekturális minta).
    * A backend-en belül például szét vannak választva az app (controller), üzleti logika (service) és a perzisztencia (repository) rétegek.
* Az események kezelésében mint például slider-ek értékei, mozgatása, panelek közti váltás stb. a JavaScript-beli eseménykezelést fogjuk használni.
* Az adatok tárolására, perzisztálására egy NoSQL adatbázist fog használni az alkalmazás, azon belül is a Redis-t.
* A weboldal biztonságát az biztosítja, hogy nincsenek semmilyen harmadik féltől származó sütik használva, amikkel azonosítani lehetne a felhasználót, illetve nincsenek is ilyen sütik elküldve a backendtől.
    * Továbbá, mivel nem tárol az alkalmazás semmilyen felhasználói adatot explicit módon, ezért nincsenek GDPR szabályszegések sem.
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
* Mint azt fentebb is említettem, az alkalmazásunk HTML-t, CSS-t, JavaScript-et illetve Python-t fog használni a működéséhez.
    * Ez által minimális, ám bár tisztán MVC-nek nem mondható, MVC architekturális mintát tudunk követni, ahol el tudjuk szeparálni egymástól a modellt, kontrollert és nézetet.
* Függőségek kezelésére nem feltétlen van szükség, illetve python-ban nem is nagyon van lehetőség különböző build tool-ok használatára, mivel az alkalmazásban csupán pár külső python module/library van használva, a *redis*, *jsonify*, *Flask*, *openCV*, *Pillow* és egyéb külső szöveges formátumba konvertáló modulok (pdf, docx, doc stb.), mindez a backend-en belül.
* Alkalmazásunk továbbá 3 különböző réteget fog tartalmazni a backend-en:
    * **Perzisztencia réteg**: ez egy python fájl lesz, ami kezeli a redis adatbázist, mely a következő funkcionalitásokkal fog rendelkezni:
        * Mint például: felhasználó regisztrálása/mentése, preset-ek mentése
    * **Üzleti logika réteg**: ez a réteg fogja végezni a különböző kép-manipulálási műveleteket (szöveg kinyerése, kép feljavítása, háttér eltávolítása)
        * Minden ilyen funkcionalitásnak, service-nek egy vagy több külön python fájl lesz rendelve.
    * **Kontroller**: ez fogja a servicek-hez irányítani a különböző beérkező HTTP kéréseket.
        * Mindezt a frontend, egy library-t használva fogja elérni (pl. *Axios* vagy *fetch API*) és hívni.
* Az előbbieknek köszönhetően pedig, szépen tudjuk követni az Egyszeres Felelősség Elvét (angolul Single Responsibility Principle - a SOLID elvekből az elsőt), ami lehetővé fogja tenni az alkalmazás egyszerűbb és átláthatóbb karbantartását.
---
## 11. Tesztterv
* Egy alkalmazás készítésekor, illetve kiadás előtt nagyon fontos szerepet játszanak a teszttervek.<br>
  A teszttervek által tudunk különféle funkciók helyes működéséről meggyőződni,<br>
  és a különféle üzleti szolgáltatások hitelességéről is.<br>
  A szoftver kiadása előtt 2 tesztet kell végrehajtani, melyek az alpha illetve beta tesztek.

* Alpha teszt
    * Fejlesztő csapat fogja elvégezni.
    * Ezen teszt során azt vizsgáljuk, hogy az alkalmazás hogyan reagál különboző böngészőkben,<br>
     és, hogy az adott funkciók működneke.
    * Ha azt látjuk, hogy az előző feltételek megfelelnek, akkor sikeres volt az alpha teszt, és jöhet majd a beta teszt.

* Beta teszt
    * A beta tesztet a fejlesztő csapattól független, kívülálló emberek végzik el.
    * Ennek a tesztnek célja az, hogy a felhasználóktól visszajelzést kapjunk, hogy <br>
      mennyire működőképes az alkalmazás.

* Amennyiben hibás működésbe ütköznek a felhasználók, akkor egy tesztelési naplóban <br>
  levezetik a tapasztalataikat, és azt visszaküldik a fejlesztőknek, a fejlesztők pedig megoldják a hibát.

* Tesztelésre használt eszközök
  Böngészők: Google Chrome , Mozilla Firefox, Microsoft Edge, Opera, Brave <br>
  Operációs rendszer: Windows 10, Ubuntu
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
* Alkalmazás telepítése
  * Fejlesztés alatt:
    * Nincs szükség telepítésre, hiszen a fejlesztő környezetből (*Visual Studio Code*) van lehetőség live server nyitására is, vagy csak egyszerűen megnyitjuk az index.html oldalt egy tetszőleges webböngészőben.
  * Deploy után:
    * Elegendő csak az előre meghatározott github-os linket megnyitni, ami automatikusan behozza és betölti a szolgáltatást.
---
## 13. Karbantartási terv
* Az alkalmazás folyamatos üzemeltetése és karbantartása, mely
magában foglalja a programhibák kijavítását, a belső igények változása miatti
módosításokat, valamint a környezeti feltételek változása miatt
megfogalmazott program-, és állomány módosítási igényeket is.
A szoftveren havonta szeretnénk karbantartásokat végezni, ezen felül bármilyen
felhasználói hibajelentés után azonnali helyreállítás jön. A szoftveren évente nagyobb
frissítések, módosítások fordulhatnak elő.
Idő elteltével új funkcionalitásokat kell hozzáadni az apphoz, hogy fent tartsuk az
érdeklődési szintet. 