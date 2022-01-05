# Kółko i krzyżyk
# Komputer gra w kółko i krzyżyk przeciwko człowiekowi

# Stałe globalne
X = 'X'
O = "O"
EMPTY = ' '
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    """Wyświetl instrukcję gry."""
    print(
        """
        Witaj w największym intelektualnym wyzwaniu wszech czasów, jakim jest
        gra 'Kółko i krzyżyk'. Będzie to ostateczna rozgrywka między Twoim
        ludzkim mózgiem a moim krzemowym procesorem.  

        Swoje posunięcie wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
        Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:

                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8

        Przygotuj się, Człowieku.  Ostateczna batalia niebawem się rozpocznie. \n
        """
    )


def ask_yes_no(question):
    """Zadaj pytanie na które można odpowiedzieć tak lub nie"""
    response = None
    while response not in ('t', 'n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Popros o podanie liczby z odpowiedniego zakresu"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Ustal, czy pierwszy ruch należy do gracza, czy do komputera."""
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu? (t/n): ")
    if go_first == "t":
        print("\nWięc pierwszy ruch należy do Ciebie.  Będzie Ci potrzebny.")
        human = X
        computer = O
    else:
        print("\nTwoja odwaga Cię zgubi... Ja wykonuję pierwszy ruch.")
        computer = X
        human = O
    return computer, human

