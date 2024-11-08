from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(
        label= "Nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Ex.:  carlos@eduardo.com'
                                          }
                            )
        
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Digite sua senha'
                                          }
                            )
)
    
class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(
        label= "Nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Ex.:  Carlos Abritta'
                                          }
                            )

    )
    email = forms.EmailField(
        label= " Email",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Ex.:  carlos@eduardo.com'
                                          }
                            )
    )

    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Digite sua senha'
                                          }
                            )
)
    
    senha_2 = forms.CharField(
        label="Confirme a senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Confirme sua senha'
                                          }
                            )
)
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()   
            if " " in nome:
                raise forms.ValidationError("O campo nome não pode conter espaços")
            
        return nome
    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
        return senha_2
