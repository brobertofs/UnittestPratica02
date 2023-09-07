class Phonebook:

    caracteres_invalidos = ['#', '@', '!', '$', '%']
    numero_invalido = 'Numero invalido'
    numero_add = 'Numero adicionado'
    nome_invalido = 'Nome invalido'
    phonebook_limpo = 'phonebook limpado'
    numero_deletado = 'Numero deletado'
    nome_nao_existe = 'Nome nao existe no Phonebook'
    numero_nao_alterado = 'Numero nao alterado'
    numero_alterado = 'Numero alterado'

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """
        Add a new contact to the phonebook
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        # 1- Melhoria nos retornos de falha, reduzindo a quantidade de if na validação dos caracteres invalidos
        # 2- Melhoria na verificação dos nomes, validando se os caracteres invalidos existe no nome
        if any(char in name for char in self.caracteres_invalidos):
            return self.nome_invalido

        # 3- Melhoria na verificação do numero invalido, validando se o comprimento é maior que 0
        if len(number) == 0:
            return self.numero_invalido

        # 4- Melhoria na verificação do nome invalido, validando se o comprimento é maior que 0
        if len(name) == 0:
            return self.nome_invalido

        # 5- Melhoria nos retornos de numero adicionado e adição do retorno para nome invalido
        if name not in self.entries:
            self.entries[name] = number
            return self.numero_add
        else:
            return self.nome_invalido

    def lookup(self, name):
        """
        Consult a name in phonebook
        :param name: name of person in string
        :return: return number of person with name
        """
        # 6- Melhoria nos retornos de falha, reduzindo a quantidade de if na validação dos caracteres invalidos
        if any(char in name for char in self.caracteres_invalidos):
            return self.nome_invalido

        # 7- Melhoria na verificação do nome invalido, validando se o comprimento é maior que 0
        if len(name) == 0:
            return self.nome_invalido

        # 8- Melhoria nos retornos do numero do nome consultado e adição do retorno para nome invalido
        if name in self.entries:
            return self.entries[name]
        else:
            return self.nome_invalido

    def get_names(self):
        """
        Consult all names in phonebook
        :return: return all names in phonebook
        """
        # 9- Melhoria na consulta de todos os nomes existentes no phonebook, retornando no formato de lista
        return list(self.entries.keys())

    def get_numbers(self):
        """
        Consult all numbers in phonebook
        :return: return all numbers in phonebook
        """
        # 10- Melhoria na consulta de todos os numeros existentes no phonebook, retornando no formato de lista
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return self.phonebook_limpo

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        # 11- Melhoria na consulta dos dados, buscando e comparando parte do nome pelos existentes no phonebook,
        # retornando no formato de lista
        result = []
        for name, number in self.entries.items():
            if len(search_name) != 0:
                if search_name in name:
                    result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """
        Retrieve all entries in the phonebook in a sorted order
        :return: return phonebook in sorted order
        """
        # 12- Melhoria na consulta dos dados, buscando e organizando todas as entradas existentes no phonebook,
        # retornando no formato de lista em ordem alfabetica
        phonebook_sorted = sorted(self.entries.items())
        return phonebook_sorted

    def get_phonebook_reverse(self):
        """
        Retrieve all entries in the phonebook in a reverse order
        :return: return phonebook in reverse sorted order
        """
        # 13- Melhoria na consulta dos dados, buscando e organizando todas as entradas existentes no phonebook,
        # retornando no formato de lista em ordem alfabetica porém em reverso
        phonebook_reverse = sorted(self.entries.items(), reverse=True)
        return phonebook_reverse

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado' if name exists, otherwise 'Nome nao existe no Phonebook'
        """
        # 14 - Melhoria no retorno caso não exista o nome no phonebook
        if name in self.entries:
            self.entries.pop(name)
            return self.numero_deletado
        else:
            return self.nome_nao_existe

    def change_number(self, name_on_phonebook, number_changed):
        """
        Change the number associated with a name in the phonebook
        :param name_on_phonebook: The name for which the number needs to be changed
        :param number_changed: The new number to be associated with the name
        :return: Return 'Numero alterado' if the name exists and the number is different,
                 otherwise 'Nome nao existe no Phonebook' or 'Numero nao alterado'
        """
        if name_on_phonebook in self.entries:
            if self.entries[name_on_phonebook] == number_changed:
                return self.numero_nao_alterado

            self.entries[name_on_phonebook] = number_changed
            return self.numero_alterado
        else:
            return self.nome_nao_existe

    def get_name_by_number(self, number_on_phonebook):
        """
        Get names associated with a specific number in the phonebook
        :param number_on_phonebook: The number for which names need to be retrieved
        :return: Return a list of dictionaries with names and the specified number
        """
        result = []
        for name, number in self.entries.items():
            if number_on_phonebook == number:
                result.append({name, number})
        return result
