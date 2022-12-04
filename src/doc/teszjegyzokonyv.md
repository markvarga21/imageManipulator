# Tesztjegyzőkönyv
| Szám | Teszteset neve | Tesztelő | Operációs rendszer | Hardware | Böngésző | Dátum | Elvárt eredmény |  Aktuális eredmény | Sikeresség |
|----- | ------------------| -------- | ------------------ | -------- | -------- |----- | --------------- | ------------------ | ---------- |
| 1. | Regisztráció | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | A rendszer regisztrálja a felhasználót |  A rendszer valóban regisztrálja a felhasználót | &#10003; |
| 2. | Bejelentkezés | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | A felhasználó be tud jelentkezni |  Az alkalmazás be tudja jelentkeztetni a felhasználót | &#10003; |
| 3. | Kijelentkezés | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | A felhasználó ki tudjon jelentkezni |  A felhasználó ki tud jelentkezni | &#10003; |
| 4. | Preset mentés | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | A felhasználó le tudja menteni a kívánt preseteket |  Le tudja menteni a felhasználó a preseteket | &#10003; |
| 5. | Egyéni preset lista | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | A felhasználó le tudja kérni az általa lementett preseteket |  A felhasználó visszakapja az által mentett preseteket | &#10003; |
| 6. | Összes preset | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | Az alkalmazás engedi megnézni az összes presetet |  A rendszer visszaadja az összes felhasználó által lementett presetek listáját | &#10003; |
| 7. | Szöveg kinyerés | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | A felhasználó ki tud nyerni szöveget egy képből |  A felhasználó ki tudja nyerni a nyers szöveget a képből | &#10003; |
| 8. | Kép szöveg kinyerés .pdf formátumba | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | A felhasználó ki tud nyerni szöveget egy képből, s azt egy PDF-ben kapja vissza |  A felhasználó ki tudja nyerni a szöveget a képből, majd le tudja menteni a PDF-et | &#10003; |
| 9. | Kép szöveg kinyerés .txt formátumba | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | A felhasználó ki tud nyerni szöveget egy képből, s azt egy TXT-ben kapja vissza |  A felhasználó ki tudja nyerni a szöveget a képből, majd le tudja menteni a TXT-t | &#10003; |
| 10. | Kép szöveg kinyerés .doc formátumba | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | A felhasználó ki tud nyerni szöveget egy képből, s azt egy DOC-ben kapja vissza |  A felhasználó ki tudja nyerni a szöveget a képből, majd le tudja menteni a DOC-ot | &#10003; |
| 11. | Zöld háttér eltávolítása | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | A felhasználó el tudja távolítani a zöld hátteret a kívánt képről |  A felhasználó valóban el tudja távolítani a zöld hátteret a képről | &#10003; |
| 12. | Háttér csere | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | A felhasználó le tudja cserélni a már kivágott képének hátterét |  A felhasználó valóban cserélni tudja a már kivágott képének hátterét | &#10003; |
| 13. | Maximum értékek | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | Le lehet kérdezni a maximum contrast, sharpness, blur és color értékeket |  Az alkalmazás visszaadja a maximum használható értékeket | &#10003; |
| 14. | Minimum értékek | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | Le lehet kérdezni a minimum contrast, sharpness, blur és color értékeket |  Az alkalmazás visszaadja a minimum használható értékeket | &#10003; |
| 15. | Érvénytelen regisztráció | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | Ha már létező felhasználónevet akarna használni a felhasználó, ne engedje a rendszer a regisztrációt |  Az alkalmazás egy hibaüzenetet küld vissza a felhasználó felé, miszerint mér foglalt az adott felhasználónév | &#10003; |
| 16. | Érvénytelen preset mentés | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | Ha nincsenek helyes módon megadva a mentési paraméterek, ne engedje menteni a preset-et |  Az API nem engedi menteni a hiánytalanul kitöltött paraméterekkel elküldött preset-eket | &#10003; |
| 17. | Érvénytelen kijelentkezés | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | Ha a felhasználó nincs bejelentkezve, nem tudja kijelentkeztetni magát |  Az API nem engedi a kijelentkeztetést, ha nincs kit kijelentkeztetni | &#10003; |
| 18. | Érvénytelen bejelentkezés | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | Ha nincs regisztrálva az adott felhasználó, ne is tudjon bejelentkezni |  Ha nem regisztrált a felhasználó, akkor nem tud bejelentkezni sem | &#10003; |
| 19. | Érvénytelen képfeljavítás | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | Ha érvénytelen értékekkel hívja meg a felhasználó a végpontot, akkor egy hibaképet kap vissza az adott hibával feliratozva |  Hibaüzenetet küld az alkalmazás érvénytelen bármely képfeljavító végpont hívásakor | &#10003; |
| 20. | Kép feljavítása | Varga József Márk | Windows 10 | Intel Core i3, 8GB DDR4 RAM, 1050ti LP | Brave | 2022.11.27 | A felhasználó fel tudja javítani a feltöltött képét |  A felhasználó fel tudja javítani és le is tudja tölteni a képét | &#10003; |
| 21. | Fájl kiválasztás | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A felhasználó tud fájlt választani |  A rendszer feldobja a fájl választást | &#10003; |
| 22. | Vezérlő panel photo retouch | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A photo retouch gomb behozza a hozzá tartozó részt |  Megjelenik a photo retouch rész a gomb lenyomásával | &#10003; |
| 23. | Vezérlő panel text extract | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A text extract gomb behozza a hozzá tartozó részt |  Megjelenik a text extract rész a gomb lenyomásával | &#10003; |
| 24. | Vezérlő panel background remove | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A background remove gomb behozza a hozzá tartozó részt |  Megjelenik a background remove rész a gomb lenyomásával | &#10003; |
| 25. | Phtoto retouch slider-ek | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A photo retouch slider-t lehet mozgatni |  A slider mozog | &#10003; |
| 26. | Photo retouch slider értékek | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A slider mozgatásával változik az érték |  A slider-hez tartozó érték változik | &#10003; |
| 27. | Text extract size érték | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A text extract-nál lehet size értéket beírni |  Be lehet írni értéket | &#10003; |
| 28. | Text extract szín | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A text extract résznél lehet színt választani |  Lehet színt választani | &#10003; |
| 29. | Output format | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | Az aktív output format háttere fehér |  A kiválasztott formátum fehér hátterű | &#10003; |
| 30. | login rész megjelenés | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A login rész helyesen jelenik meg |  A login rész megfelelően jelenik meg | &#10003; |
| 31. | Register rész megjelenés | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A register rész jól jelenik meg |  A register rész megfelelően jelenik meg | &#10003; |
| 32. | Fő oldal megjelenés | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A fő oldal az elvártnak megfelelően jelenik meg | A fő oldal jól jelenik meg | &#10003; |
| 33. | Kép nevének átírása | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | Lehet a kép nevét változtatni |  A kép nevét átlehet írni | &#10003; |
| 34. | Kiírja a bejelentkezett személyt | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | Az oldal kiírja ki van bejelentkezve |  Alert ablakban megjelenik hogy ki van belépve | &#10003; |
| 35. | Photo retouch rész megjelenés | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A photo retouch rész az elvártnak megfelelően jelenik e meg |  A panel megfelelően jelenik meg | &#10003; |
| 36. | Text extract megjelenés | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A ext extract rész az elvártnak megfelelően jelenik e meg |  A panel megfelelően jelenik meg | &#10003; |
| 37. | Background remove megjelenés | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A background remove rész az elvártnak megfelelően jelenik e meg |  A panel megfelelően jelenik meg | &#10003; |
| 38. | Text extract slider | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A text extract sliderek mozognak e |  A slider-ek mozognak | &#10003; |
| 39. | Text extract slider érték | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A text extract slider-ek kiírják értékeiket |  Igen kiírják | &#10003; |
| 40. | Home gomb | Cserés Gábor | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1050ti | Google Chrome | 2022.11.27 | A home gomb a login részre dob e |  A gomb behozza a login részt | &#10003; |
| 41. | Download gomb | Bódi András | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1650ti | Google Chrome | 2022.12.04 | Felhoz 1 alertet, hogy mentsem le másként |  Behozza az alertet | &#10003; |
| 42. | Full screen gomb | Bódi András | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1650ti | Google Chrome | 2022.12.04 | Megnyitja teljes képernyőn |  Megnyitja teljes képernyőn | &#10003; |
| 43. | Fájl kiválasztás | Bódi András | Windows 10 | Intel Core i5, 16GB DDR4 RAM, 1650ti | Google Chrome | 2022.12.04 | Azt a képet fogja betölteni, amire kattintok |  Azt is tölti be | &#10003; |


44. 
Nem képet választok ki hanem txt-t
Bódi András
Windows 10
Intel Core i5, 16GB DDR4 RAM, 1650ti
Google Chrome 
2022.12.04
Nem fogja betölteni 
Nem tölti be
✓ 

45.
Nem képet választok ki hanem txt-t
Bódi András
Windows 10
Intel Core i5, 16GB DDR4 RAM, 1650ti
Google Chrome 
2022.12.04
Nem fogja betölteni 
Nem tölti be
✓ 

46.
Nem képet választok ki hanem exel táblázatot
Bódi András
Windows 10
Intel Core i5, 16GB DDR4 RAM, 1650ti
Google Chrome 
2022.12.04
Nem fogja betölteni 
Nem tölti be
✓ 

47.
Nem képet választok ki hanem 1 doc fájlt 
Bódi András
Windows 10
Intel Core i5, 16GB DDR4 RAM, 1650ti
Google Chrome 
2022.12.04
Nem fogja betölteni 
Nem tölti be
✓ 

48.
Bal oldalon a 2. ikont választom ki
Bódi András
Windows 10
Intel Core i5, 16GB DDR4 RAM, 1650ti
Google Chrome 
2022.12.04
Be fogja hozni a kívánt menüt 
Be is hozza 
✓ 

49.
Bal oldalon az alsó ikont választom ki
Bódi András
Windows 10
Intel Core i5, 16GB DDR4 RAM, 1650ti
Google Chrome 
2022.12.04
Be fogja hozni a kívánt menüt 
Be is hozza 
✓ 

50.
Jobb gombbal a képre kattintok 
Bódi András
Windows 10
Intel Core i5, 16GB DDR4 RAM, 1650ti
Google Chrome 
2022.12.04
Behozza a képpel kapcsolatos opciókat 
Behozza 
✓ 

51.
Menteni akarom a képet
Bódi András
Windows 10
Intel Core i5, 16GB DDR4 RAM, 1650ti
Google Chrome 
2022.12.04
Lementi a képet
Ha rákattintok jobb gomb után, hogy kép mentése másként valóban lementi a képet 
✓ 

52.
A Login a képszerkesztő oldalra visz-e?
Bódi András
Windows 10
Intel Core i5, 16GB DDR4 RAM, 1650ti
Google Chrome 
2022.12.04
Átvisz az index.html-re
Valóban átvisz
✓ 

53.
Mit csinál ha a profilikonra megyek?
Bódi András
Windows 10
Intel Core i5, 16GB DDR4 RAM, 1650ti
Google Chrome 
2022.12.04
Valamivel jelzi, hogy ki van bejelentkezve 
Valóban jelzi 1 alerttel 
✓