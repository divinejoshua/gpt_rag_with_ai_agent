from decouple import config
import os
os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')


print(os.environ['OPENAI_API_KEY'] )