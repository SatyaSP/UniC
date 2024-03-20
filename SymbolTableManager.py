class SymbolTableManager(object):
    ''' Manages the symbol table of the compiler 
        which is used across modules '''
    _global_funcs = [{
        "lexim": "printf",
        "scope": 0,
        "type": "void",
        "role": "function",
        "arity": 1,
        "params": ["int", "char", "string", "float", "double", "bool", "void"]
    }]

    @classmethod
    def init(self):
        self.scope_stack = [0]
        self.temp_stack = [0]
        self.arg_list_stack = []
        self.symbol_table = self._global_funcs.copy()
        self.declaration_flag = False
        self.error_flag = False

    @classmethod
    def scope(self):
        return len(self.scope_stack) - 1

    @classmethod
    def insert(self, lexim):
        self.symbol_table.append({"lexim" : lexim, "scope" : self.scope()})

    @classmethod
    def _exists(self, lexim, scope):
        for row in self.symbol_table:
            if row["lexim"] == lexim and row["scope"] == scope:
                return True
        return False

    @classmethod
    def findrow(self, value, attr="lexim"):
        for i in range(len(self.symbol_table) - 1, -1, -1): 
            row = self.symbol_table[i]
            if row[attr] == value:
                return row
        return None

    @classmethod
    def findrow_idx(self, value, attr="lexim"):
        for i in range(len(self.symbol_table) - 1, -1, -1): 
            row = self.symbol_table[i]
            if row[attr] == value:
                return i
        return None
    
    @classmethod
    def install_id(self, lexim):
        if not self.declaration_flag:
            i = self.findrow_idx(lexim)
            if i is not None:
                return i
        return len(self.symbol_table)

    @classmethod
    def get_enclosing_fun(self, level=1):
        try:
            return self.symbol_table[self.scope_stack[-level] - 1]
        except IndexError:
            return None