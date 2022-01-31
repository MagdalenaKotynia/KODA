<p style="text-align: center;"><strong><span style="font-size: 20px;">Projekt KODA</span></strong></p>
<p style="text-align: center;"><strong>Kodowanie r&oacute;żnicowe + kodowanie Huffmana</strong></p>
<p style="text-align: center;"><strong>prowadzący: dr inż. Andrzej Buchowicz</strong></p>
<ul>
    <li>Opracować algorytm kodowania predykcyjnego danych dwuwymiarowych wykorzystując do predykcji:<ul>
            <li><span id="isPasted" style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>lewego</span> sąsiada,</li>
            <li><span id="isPasted" style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>g&oacute;rnego sąsiada,</span></li>
            <li>medianę lewego, lewego-g&oacute;rnego, g&oacute;rnego sąsiada.</li>
        </ul>
    </li>
    <li>Wyznaczyć histogramy i entropie danych wejściowych i r&oacute;żnicowych dla sztucznie wygenerowanych ciąg&oacute;w danych wejściowych o rozkładzie r&oacute;wnomiernym, normalnym, Laplace&apos;a oraz obraz&oacute;w testowych.</li>
    <li>Zakodować dane r&oacute;żnicowe przy użyciu klasycznego algorytmu Huffmana.</li>
    <li>Por&oacute;wnać entropię ze średnią długością bitową kodu wyjściowego.</li>
    <li>Ocenić efektywność algorytmu do kodowania obraz&oacute;w naturalnych.</li>
</ul>
<p><strong>Struktura projektu:</strong></p>
<p><em>Kody algotym&oacute;w:</em></p>
<p>/modules - folder zawiera gł&oacute;wną część projektu, kt&oacute;ra zawiera algorytmy jak i funkcje testujące:</p>
<ul>
    <li>data_generator.py - program generuje dwuwymiarowe dane o rozkładzie normalnym, jednostkowym i Laplaca.</li>
    <li>experiments.py - program obliczający wszystkie statystyki dotyczące algorytm&oacute;w czyli średnią entropię, dlugość słowa kodowego oraz redundancję</li>
    <li>huffman_codec.py - program realizujący algorytm konstrukcji drzewa Huffmana</li>
    <li>predictive_coder.py - program koduje i dekoduje obraz przy użyciu algorytmu predykcyjnego</li>
    <li>tests_huffman_codec.py - moduł zawierający testy jednostkowe funkcji Huffmana</li>
    <li>utils.py - moduł wyliczający entropię oraz histogramy</li>
</ul>
<p><em>Paczki ze zdjęciami testowymi:</em></p>
<p>/test_images - lista naturalnych obraz&oacute;w testowych</p>
<p>/my_test_images - lista własnych obraz&oacute;w testowych</p>
<p>/generated_test_data - lista sztucznie wygenerowanych obraz&oacute;w testowych wykorzystanych do por&oacute;wnania z otrzymanymi danymi</p>
<p>/histograms - lista z wygenerowanymi histogramami każdego testowanego obrazu</p>
<p>Pozostałe foldery /__pycache__ oraz .idea są konieczne do działania powyższych program&oacute;w</p>
<p><strong>Wyb&oacute;r narzędzi programistycznych:</strong></p>
<p><strong>Python, używane biblioteki:</strong></p>
<p>Numpy&nbsp;</p>
<p>Matplotlib&nbsp;</p>
<p>PIL/scikit-image</p>
<p><strong>Metody oceny efektywności:</strong></p>
<ul>
    <li>wsp&oacute;łczynnik kompresji</li>
    <li>entropia</li>
    <li>średnia długość bitowa kodu wyjściowego</li>
</ul>
<p><strong>Bibliografia:</strong></p>
<p>Artur Przelaskowski, Kompresja danych. Podstawy. Metody bezstratne. Kodery obraz&oacute;w., Wydawnictwo BTC, 2005</p>
<p>K. Sayood, Kompresja danych - wprowadzenie, Wydawnictwo RM, 2002</p>
