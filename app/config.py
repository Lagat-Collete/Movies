class Config:
  '''
  General configuration parent class
  '''
  MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/550?api/movie/{}?api_key={}'
  pass

class ProdConfig(Config):
  '''
  production configuration child class
  
  Args:
      Config: The parent configuration class with Geberal configuratin settings
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class
  Args:
  Config: The parent configuration class with General configuration settings
  '''
  DEBUG = True
