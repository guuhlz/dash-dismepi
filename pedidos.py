import pandas as pd

desc_produtos = pd.read_excel('./data/desc_produtos.xlsx',sheet_name='Prod')

class Pedido:
    def __init__(self,arquivo_caminho):
        self.arquivo_caminho = arquivo_caminho
        self.df = pd.read_excel(self.arquivo_caminho, sheet_name='PEDIDO')

        desc_produtos = pd.read_excel('./data/desc_produtos.xlsx',sheet_name='Prod')
        self.df = self.df.merge(desc_produtos,on='Código Promax',how='outer')

    def __estoque_no_mktp(self):
        return self.df[self.df['Categorização'] != '003 - MKTP'][['Prod_resume', 
                                                                  'IMPACTO', 
                                                                  'OVER/DOWN',
                                                                  'PERCENTUAL OVER/DOWN',
                                                                  'Estoque HL',
                                                                  'Prod. Completo',
                                                                  'FEFO/ESTOQUE',
                                                                  'FEFO/PICKING']]

    def estoque_over(self):
        estoque_over = self.df[self.df['OVER/DOWN'] > 0]['OVER/DOWN'].sum() 
        return estoque_over
    
    def estoque_down(self):
        estoque_down = self.df[self.df['OVER/DOWN'] < 0]['OVER/DOWN'].sum()
        return estoque_down
    
    def estoque_maximo(self):
        estoque_maximo = self.df[self.df['ESTOQUE MÁXIMO'] > 0]['ESTOQUE MÁXIMO'].sum()
        return estoque_maximo

    def estoque_minimo(self):
        estoque_minimo = self.df[self.df['ESTOQUE MÍNIMO'] > 0]['ESTOQUE MÍNIMO'].sum()
        return estoque_minimo
    
    def estoque_real(self):
        estoque_minimo = self.df[self.df['ESTOQUE REAL'] > 0]['ESTOQUE REAL'].sum()
        return estoque_minimo
    
    def estoque_ambev_hl(self):
        df_no_mktp = self.__estoque_no_mktp()
        estoque_hl = df_no_mktp['Estoque HL'].sum()
        return round(estoque_hl)
    
    def estoque_top10_impacto_over(self):
        df_no_mktp = self.__estoque_no_mktp()
        estoque_top10_impacto_over = df_no_mktp.sort_values(by=['IMPACTO'], ascending=False).head(10)
        return estoque_top10_impacto_over
    
    def estoque_top10_impacto_down(self):
        df_no_mktp = self.__estoque_no_mktp()
        estoque_top10_impacto_down = df_no_mktp.sort_values(by=['IMPACTO'], ascending=True).head(10)
        return estoque_top10_impacto_down

    def estoque_top10_percentual_over(self):
        df_no_mktp = self.__estoque_no_mktp()
        estoque_top10_percentual_over = df_no_mktp.sort_values(by=['PERCENTUAL OVER/DOWN'], ascending=False).head(10)
        estoque_top10_percentual_over['PERCENTUAL OVER/DOWN'] *= 100
        return estoque_top10_percentual_over

    def estoque_top10_percentual_down(self):
        df_no_mktp = self.__estoque_no_mktp()
        estoque_top10_percentual_down = df_no_mktp.sort_values(by=['PERCENTUAL OVER/DOWN'], ascending=True).head(10)
        estoque_top10_percentual_down['PERCENTUAL OVER/DOWN'] *= 100
        return estoque_top10_percentual_down
    
    def estoque_mktp_valor(self):
        return self.df[self.df['Categorização'] == '003 - MKTP']['ESTOQUE REAL'].sum()