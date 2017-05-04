module StaticPagesHelper
  class Recipe
    attr_accessor :name, :url, :image, :id
  end

  def create_ingredients_cookie(ingredients)
    cookies[:ingredients] = { :value => ingredients.join(','), :expires => 1.year.from_now }
  end

  def get_ingredients_from_cookie
    if not cookies[:ingredients].nil? 
      return cookies[:ingredients].split(',')
    else
      return []
    end
  end

end
