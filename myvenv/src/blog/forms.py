from django import forms

from .models import Article

# class ArticleForm(forms.ModelForm):
# 	title 		= forms.CharField(label='', 
# 					widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
# 	content = forms.CharField(
# 						required=False, 
# 						widget = forms.Textarea(
# 							attrs={
# 								"placeholder": "Your Content",
# 								"class":  "new-class-name two",
# 								"id": "my-id-for-textarea",
# 								"rows":10,
# 								"cols":120
# 							}
# 						))
# 	active 		= forms.BooleanField(default = True)
class ArticleModelForm(forms.ModelForm):	
	class Meta:
		model = Article
		fields = [
			'title',
			'content',
			'active'
		]