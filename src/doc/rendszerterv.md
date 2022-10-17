# **Rendszerterv**
## 1. A rendszer célja
* A rendszer célja, hogy a felhasználó képet tudjon beolvasni, és különböző műveleteket megcsinálni rajta. Pl.:
  * Tudja a kép kontrasztját javítani
  * Tudja a kép élességét feljavítani
  * Tudja a kép homályosságát állítani
  * Tudja a fényességet csökkenteni
  * Tudja a fényességet növelni
  * Át tudja méretezni a képet
  * Ki tudjon nyerni a képből karaktert és azt törölni a képről
  * A felhasználó át tudja convertálni a képet: doc, pdf, docx stb. formátummá 
  * A felhasználó le tudja szedni a hátteret
  * A felhasználó hozzátudjon adni hátteret a képhez
  * A felhasználó egy felhasználónév megadásával tudjon bejelentkezni
  * A felhasználó le tudja menteni a saját preset-jeit
  * A felhasználó le tudja menteni az elkészült képet a változtatásokkal
* Fontos, hogy a felület bárhol elérhető legyen, ott is ahol internet szolgáltatás nem elérhető, <br>
  ezért webes felületen kívül bármilyen, kliens által választott okos eszközökre is telepíthető legyen. <br>
* Annak érdekében, hogy átlátható mlegyen az alkalmazás, a design-ra elég nagy figyelmet szentelünk. <br>
  A mostanában divatos reszponzív design-t fogjuk használni. <br>
* A cél egy olyan oldal létrehozása amegy bárki számára bármikor rendelkezésre áll a neten.
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
    * A backendhez python flaskot, reddist, opencv-t használunk.
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
  és a különféle üzleti szolgáltatások hitelesítéséről is.<br>
  A szoftver kiadása előtt 2 tesztet kell végrehajtani, melyek az alpha illetve beta tesztek.

* Alpha teszt
    * Fejlesztő csapat fogja elvégezni.
    * Ezen teszt során azt vizsgáljuk, hogy az alkalmazás hogyan reagál különboző böngészőkben,<br>
     és az adott funkciók működneke.
    * Ha azt látjuk, hogy az előző feltételek megfelelnek, akkor sikeres volt az alpha teszt, és jöhet majd a beta teszt.

* Beta teszt
    * A beta tesztet a fejlesztő csapattól független, kívülálló emberek végzik el.
    * Ennek a tesztnek célja az, hogy a felhasználóktól visszajelzést kapjunk, hogy a <br>
      mennyire működőképes az alkalmazás.

* Amennyiben hibás működésbe ütköznek a felhasználók, akkor egy tesztelési naplóban <br>
  levezetik a tapasztalataikat, és azt visszaküldik a fejlesztőknek, a fejlesztők pedig megoldják a hibát.

* Tesztelésre használt eszközök
  Böngészők: Google Chrome , Mozilla Firefox, Microsoft Edge, Opera <br>
  Operációs rendszer: Windows 10, Ubuntu
---
## 12. Telepítési terv
---
## 13. Karbantartási terv
