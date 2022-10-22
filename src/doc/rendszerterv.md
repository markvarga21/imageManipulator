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
---
## 9. Adatbázis terv
---
## 10. Implementációs terv
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