class TextProcessor:
    def __init__(self, text):
        self.original_text = text
        self.current_text = text
        self.history = []

    def count_characters(self):
        char_count = {}
        for char in self.current_text:
            if char == '\n':  # Ignorar los saltos de línea
                continue
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count

    def substitute_character(self, old_char, new_char):
        # Guardar el texto antes del cambio en el historial para poder deshacerlo después
        self.history.append(self.current_text)
        self.current_text = self.current_text.replace(old_char, new_char)
        print(f'Se ha sustituido "{old_char}" por "{new_char}".')

    def undo_last_change(self):
        if self.history:
            self.current_text = self.history.pop()
            print("Último cambio deshecho.")
        else:
            print("No hay cambios para deshacer.")

    def show_text(self):
        print(f"Texto actual: {self.current_text}")


# Menú de opciones
def menu():
    while True:
        print("\nOpciones:")
        print("1. Contar repeticiones de caracteres")
        print("2. Sustituir un carácter por otro")
        print("3. Deshacer el último cambio")
        print("4. Mostrar el texto actual")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            char_count = processor.count_characters()
            print("\nRepeticiones de cada carácter:")
            for char, count in char_count.items():
                print(f"'{char}': {count}")
        elif opcion == "2":
            old_char = input("Ingresa el carácter que deseas sustituir: ")
            new_char = input("Ingresa el nuevo carácter: ")
            processor.substitute_character(old_char, new_char)
        elif opcion == "3":
            processor.undo_last_change()
        elif opcion == "4":
            processor.show_text()
        elif opcion == "5":
            # Confirmando 2 veces
            confirmacion_1 = input("¿Estás seguro que deseas salir? (s/n): ").lower()
            if confirmacion_1 == "s":
                confirmacion_2 = input("¿Estás realmente seguro? (s/n): ").lower()
                if confirmacion_2 == "s":
                    print("Saliendo del programa.")
                    break
                else:
                    print("Cancelando la salida.")
            else:
                print("Cancelando la salida.")
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


# Texto hardcodeado
text = """ 
RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE 
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
 AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ 
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX 
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, 
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN 
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, 
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK 
HKCZJOI OKEJSZCNHE.
"""


if __name__ == '__main__':
    # Crear una instancia del procesador de texto
    processor = TextProcessor(text)
    # Ejecutar el menú
    menu()
