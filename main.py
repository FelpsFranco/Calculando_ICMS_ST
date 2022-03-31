# Cálculo ICMS ST

from tkinter import *
from tkinter import ttk


class Main:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('800x400')
        self.janela.resizable(width=False, height=False)
        self.janela.title('Calculando ICMS-ST')
        self.janela.configure(bg='brown')

        # ICMS
        # ---------------------------------------------------------------------------------------------------------------#

        self.total_base_icms = Label(self.janela, text='Base ICMS: ', fg='white', bg='black')
        self.total_base_icms.place(x=30, y=10, width=130)
        self.insere_valor_base = Entry(self.janela, bg='white', fg='black')
        self.insere_valor_base.place(x=170, y=10, width=180, height=21)

        self.info0 = Button(self.janela, text=' ? ', command=self.info_produtos)
        self.info0.place(x=7, y=11, width=20, height=19)

        self.info_valor_icms = Label(self.janela, text='Valor ICMS Inter:', bg='black', fg='white')
        self.info_valor_icms.place(x=400, y=10, width=130)
        self.valor_icms = Label(self.janela, text='', bg='white', fg='black')
        self.valor_icms.place(x=540, y=10, width=180, height=21)

        self.info1 = Button(self.janela, text=' ? ', command=self.info_produtos)
        self.info1.place(x=378, y=11, width=20, height=19)

        # ---------------------------------------------------------------------------------------------------------------#

        # Configuração de Alíquota ICMS
        # ---------------------------------------------------------------------------------------------------------------#

        self.vlist_origin = ['Estado Origem', 'AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS',
                             'MT', 'PA', 'PB',
                             'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
        self.list_estado_orig = ttk.Combobox(self.janela, values=self.vlist_origin)
        self.list_estado_orig.set('Estado Origem')
        self.list_estado_orig.place(x=30, y=50)

        self.vlist_dest = ['Estado Destino', 'AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS',
                           'MT', 'PA', 'PB',
                           'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
        self.list_estado_dest = ttk.Combobox(self.janela, values=self.vlist_dest)
        self.list_estado_dest.set('Estado Destino')
        self.list_estado_dest.place(x=30, y=80)

        self.set = Button(self.janela, command=self.set_aliq, text='Ok')
        self.set.place(x=200, y=81, width=25, height=20)

        self.valor_aliquota_inter = Label(self.janela, text='Alíquota Inter (%):     ', fg='white', bg='black')
        self.valor_aliquota_inter.place(x=30, y=120, width=130)
        self.insere_aliquota_inter = Entry(self.janela, bg='white', fg='black')
        self.insere_aliquota_inter.place(x=170, y=120, width=180, height=21)

        self.valor_aliquota_intra = Label(self.janela, text='Alíquota Intra (%):     ', fg='white', bg='black')
        self.valor_aliquota_intra.place(x=400, y=120, width=130)
        self.insere_aliquota_intra = Entry(self.janela, bg='white', fg='black')
        self.insere_aliquota_intra.place(x=540, y=120, width=180, height=21)

        # ---------------------------------------------------------------------------------------------------------------#

        # Outras Alíquotas
        # ---------------------------------------------------------------------------------------------------------------#

        self.info2 = Button(self.janela, text=' ? ', command=self.info_mva)
        self.info2.place(x=7, y=201, width=20, height=19)

        self.valor_mva = Label(self.janela, text='MVA (%):', fg='white', bg='black')
        self.valor_mva.place(x=30, y=200, width=130)
        self.insere_mva = Entry(self.janela, bg='white', fg='black')
        self.insere_mva.place(x=170, y=200, width=180, height=21)

        self.info3 = Button(self.janela, text=' ? ', command=self.info_ipi)
        self.info3.place(x=7, y=241, width=20, height=19)

        self.valor_ipi = Label(self.janela, text='Valor IPI:', fg='white', bg='black')
        self.valor_ipi.place(x=30, y=240, width=130)
        self.insere_ipi = Entry(self.janela, bg='white', fg='black')
        self.insere_ipi.place(x=170, y=240, width=180, height=21)

        # ---------------------------------------------------------------------------------------------------------------#

        # Chamando a Função de Cálulo
        # ---------------------------------------------------------------------------------------------------------------#

        self.resultado = Button(self.janela, command=self.calcula, text='Resultado', bg='black', fg='white')
        self.resultado.place(x=30, y=280)

        # ---------------------------------------------------------------------------------------------------------------#

        # Entrada de dados já Calculado
        # ---------------------------------------------------------------------------------------------------------------#

        self.info4 = Button(self.janela, text=' ? ', command=self.info_st)
        self.info4.place(x=7, y=361, width=20, height=19)

        self.base_st = Label(self.janela, text='Base ICMS ST:', bg='black', fg='white')
        self.base_st.place(x=30, y=360, width=130)
        self.calculo_base_st = Label(self.janela, text='', bg='white', fg='black')
        self.calculo_base_st.place(x=170, y=360, width=180, height=21)

        self.info5 = Button(self.janela, text=' ? ', command=self.info_valor_st)
        self.info5.place(x=378, y=361, width=20, height=19)

        self.valor_st = Label(self.janela, text='Valor ICMS ST:', bg='black', fg='white')
        self.valor_st.place(x=400, y=360, width=130)
        self.calculo_valor_st = Label(self.janela, text='', bg='white', fg='black')
        self.calculo_valor_st.place(x=540, y=360, width=180, height=21)

        # ---------------------------------------------------------------------------------------------------------------#

        # Loop TK para manter a Janela aberta
        # ---------------------------------------------------------------------------------------------------------------#

        self.janela.mainloop()

        # ---------------------------------------------------------------------------------------------------------------#

    # Função de Cálculo Valor ICMS e Valor ST | Chamado pelo Button Resultado | Absorve os GETs e gera resultado
    # -------------------------------------------------------------------------------------------------------------------#
    def calcula(self):
        if self.insere_ipi.get() == '':
            self.insere_ipi.insert(0, '0')

        if self.insere_mva.get() == '':
            self.insere_mva.insert(0, '0')

        valor_produto = self.insere_valor_base.get()
        valor_produto = float(valor_produto)

        inter = self.insere_aliquota_inter.get()
        inter = float(inter)
        intra = self.insere_aliquota_intra.get()
        intra = float(intra)

        valor_icms = valor_produto * inter / 100
        self.valor_icms['text'] = valor_icms

        mva = self.insere_mva.get()
        mva = float(mva)
        ipi = self.insere_ipi.get()
        ipi = float(ipi)

        base_st = (valor_produto + ipi) * (1 + (mva / 100))
        self.calculo_base_st['text'] = base_st

        valor_st = (base_st * (intra / 100)) - valor_icms
        valor_st = round(valor_st, 3)
        if valor_st < 0:
            valor_st = 0
            self.calculo_valor_st['text'] = valor_st
        self.calculo_valor_st['text'] = valor_st

    # -------------------------------------------------------------------------------------------------------------------#

    # Informações para Usuário
    # ------------------------------------------------------------------------------------------------------------------#

    def info_produtos(self):
        self.mensagem = Tk()
        self.mensagem.geometry('650x100')
        self.mensagem.resizable(width=False, height=False)
        self.mensagem.configure(bg='black')
        self.mensagem.title('Informação')

        label_erro = Label(self.mensagem, image="::tk::icons::question", bg='black')
        label_erro.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
        label_mensagem = Label(self.mensagem,
                               text="Base do ICMS Inter = (Valor do produto + Frete + Seguro + Outras Despesas Acessórias - Descontos) ",
                               bg='black', fg='white')
        label_mensagem.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")

        b1 = Button(self.mensagem, text="OK", command=self.mensagem.destroy, width=4, bg='white', borderwidth=0)
        b1.grid(row=1, column=1, padx=(200, 200), sticky="e")

    # -------------------------------------------------------------------------------------------------------------------#

    def info_st(self):
        self.mensagem = Tk()
        self.mensagem.geometry('850x100')
        self.mensagem.resizable(width=False, height=False)
        self.mensagem.configure(bg='black')
        self.mensagem.title('Informação')
        label_erro = Label(self.mensagem, image="::tk::icons::question", bg='black')
        label_erro.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
        label_mensagem = Label(self.mensagem,
                               text="Base do ICMS ST = (Valor do produto + Valor do IPI + Frete + Seguro + Outras Despesas Acessórias - Descontos) * (1+(%MVA / 100)) ",
                               bg='black', fg='white')
        label_mensagem.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
        b1 = Button(self.mensagem, text="OK", command=self.mensagem.destroy, width=4, bg='white', borderwidth=0)
        b1.grid(row=1, column=1, padx=(250, 250), sticky="e")

    # -------------------------------------------------------------------------------------------------------------------#

    def info_valor_st(self):
        self.mensagem = Tk()
        self.mensagem.geometry('650x100')
        self.mensagem.resizable(width=False, height=False)
        self.mensagem.configure(bg='black')
        self.mensagem.title('Informação')
        label_erro = Label(self.mensagem, image="::tk::icons::question", bg='black')
        label_erro.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
        label_mensagem = Label(self.mensagem,
                               text="Valor do ICMS ST = (Base do ICMS ST * (Alíquota do ICMS Intra / 100)) - Valor do ICMS Inter ",
                               bg='black', fg='white')
        label_mensagem.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
        b1 = Button(self.mensagem, text="OK", command=self.mensagem.destroy, width=4, bg='white', borderwidth=0)
        b1.grid(row=1, column=1, padx=(150, 150), sticky="e")

    # -------------------------------------------------------------------------------------------------------------------#

    def info_mva(self):
        self.mensagem = Tk()
        self.mensagem.geometry('650x100')
        self.mensagem.resizable(width=False, height=False)
        self.mensagem.configure(bg='black')
        self.mensagem.title('Informação')
        label_erro = Label(self.mensagem, image="::tk::icons::question", bg='black')
        label_erro.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
        label_mensagem = Label(self.mensagem,
                               text="Margem de Valor Agregado é uma espécie de margem de lucro para cada produto ou um conjunto deles.",
                               bg='black', fg='white')
        label_mensagem.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
        b1 = Button(self.mensagem, text="OK", command=self.mensagem.destroy, width=4, bg='white', borderwidth=0)
        b1.grid(row=1, column=1, padx=(150, 150), sticky="e")

    # -------------------------------------------------------------------------------------------------------------------#

    def info_ipi(self):
        self.mensagem = Tk()
        self.mensagem.geometry('650x100')
        self.mensagem.resizable(width=False, height=False)
        self.mensagem.configure(bg='black')
        self.mensagem.title('Informação')
        label_erro = Label(self.mensagem, image="::tk::icons::question", bg='black')
        label_erro.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
        label_mensagem = Label(self.mensagem,
                               text="O IPI é um imposto que incide sobre itens nacionais e importados que foram produzidos industrialmente ou passaram por algum processo de industrialização.",
                               bg='black', fg='white')
        label_mensagem.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
        b1 = Button(self.mensagem, text="OK", command=self.mensagem.destroy, width=4, bg='white', borderwidth=0)
        b1.grid(row=1, column=1, padx=(150, 150), sticky="e")

    # -------------------------------------------------------------------------------------------------------------------#

    def set_aliq(self):
        print(self.list_estado_orig.get())
        print(self.list_estado_dest.get())
        if self.list_estado_dest.get() == 'SP' and self.list_estado_orig.get() == 'SP':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'AC' and self.list_estado_orig.get() == 'AC':
            return self.insere_aliquota_inter.insert(0, '17'), self.insere_aliquota_intra.insert(0, '17')

        if self.list_estado_dest.get() == 'AL' and self.list_estado_orig.get() == 'AL':
            return self.insere_aliquota_inter.insert(0, '12'), self.insere_aliquota_intra.insert(0, '12')

        if self.list_estado_dest.get() == 'AM' and self.list_estado_orig.get() == 'AM':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'AP' and self.list_estado_orig.get() == 'AP':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'BA' and self.list_estado_orig.get() == 'BA':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'CE' and self.list_estado_orig.get() == 'CE':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'DF' and self.list_estado_orig.get() == 'DF':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'ES' and self.list_estado_orig.get() == 'ES':
            return self.insere_aliquota_inter.insert(0, '17'), self.insere_aliquota_intra.insert(0, '17')

        if self.list_estado_dest.get() == 'GO' and self.list_estado_orig.get() == 'GO':
            return self.insere_aliquota_inter.insert(0, '17'), self.insere_aliquota_intra.insert(0, '17')

        if self.list_estado_dest.get() == 'MA' and self.list_estado_orig.get() == 'MA':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'MT' and self.list_estado_orig.get() == 'MT':
            return self.insere_aliquota_inter.insert(0, '17'), self.insere_aliquota_intra.insert(0, '17')

        if self.list_estado_dest.get() == 'MS' and self.list_estado_orig.get() == 'MS':
            return self.insere_aliquota_inter.insert(0, '17'), self.insere_aliquota_intra.insert(0, '17')

        if self.list_estado_dest.get() == 'MG' and self.list_estado_orig.get() == 'MG':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'PA' and self.list_estado_orig.get() == 'PA':
            return self.insere_aliquota_inter.insert(0, '17'), self.insere_aliquota_intra.insert(0, '17')

        if self.list_estado_dest.get() == 'PB' and self.list_estado_orig.get() == 'PB':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'PR' and self.list_estado_orig.get() == 'PR':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'PE' and self.list_estado_orig.get() == 'PE':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'PI' and self.list_estado_orig.get() == 'PI':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'RN' and self.list_estado_orig.get() == 'RN':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'RS' and self.list_estado_orig.get() == 'RS':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'RJ' and self.list_estado_orig.get() == 'RJ':
            return self.insere_aliquota_inter.insert(0, '20'), self.insere_aliquota_intra.insert(0, '20')

        if self.list_estado_dest.get() == 'RO' and self.list_estado_orig.get() == 'RO':
            return self.insere_aliquota_inter.insert(0, '17.5'), self.insere_aliquota_intra.insert(0, '17.5')

        if self.list_estado_dest.get() == 'RR' and self.list_estado_orig.get() == 'RR':
            return self.insere_aliquota_inter.insert(0, '17'), self.insere_aliquota_intra.insert(0, '17')

        if self.list_estado_dest.get() == 'SC' and self.list_estado_orig.get() == 'SC':
            return self.insere_aliquota_inter.insert(0, '17'), self.insere_aliquota_intra.insert(0, '17')

        if self.list_estado_dest.get() == 'SE' and self.list_estado_orig.get() == 'SE':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_dest.get() == 'TO' and self.list_estado_orig.get() == 'TO':
            return self.insere_aliquota_inter.insert(0, '18'), self.insere_aliquota_intra.insert(0, '18')

        if self.list_estado_orig.get() == 'SP' and self.list_estado_dest.get() == 'AC' or 'AL' or 'AP' or 'BA' or 'CE' \
                or 'DF' or 'ES' or 'GO' or 'MA' or 'MT' or 'MS':
            print('ok')
            return self.insere_aliquota_inter.insert(0, '7'), self.insere_aliquota_intra.insert(0, '7')

        if self.list_estado_orig.get() == 'SP' and self.list_estado_dest.get() == 'MG' or 'PR' or 'RS' or 'RJ' or 'SC':
            print('nada')
            return self.insere_aliquota_inter.insert(0, '12'), self.insere_aliquota_intra.insert(0, '12')


Main()