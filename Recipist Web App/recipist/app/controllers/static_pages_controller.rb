class StaticPagesController < ApplicationController
  include StaticPagesHelper
  require 'net/http'
  require 'rubygems'
  require 'json'

  def home
    @ingredients = get_ingredients_from_cookie()
  end

  def search
    # Parse ingredients to array
    @ingredients = []
    params.each do |key,value|
      if key.include? "ingrs"
        @ingredients = value.split(',')
      end
    end

    # Make cookie or get ingredients from cookie
    if @ingredients.empty?
      @ingredients = get_ingredients_from_cookie()
    else
      create_ingredients_cookie(@ingredients)
    end

    # Create search URL
    tmp_url = 'http://recipist-csci3308.herokuapp.com/search?ingrds='
    @ingredients.each do |ingr|
      tmp_url += ingr + ','
    end

    url = URI.parse(tmp_url)
    req = Net::HTTP::Get.new(url.to_s)
    res = Net::HTTP.start(url.host, url.port) {|http|
      http.request(req)
    }

    # Parse JSON recipes
    data = JSON.parse(res.body)
    @recipes = []
    ids = []
    data.each do |r|
      recipe = Recipe.new
      recipe.name   = r['Name']
      recipe.id     = r['Id']
      recipe.url    = r['url']
      recipe.image  = r['image_url']

      if not ids.include? recipe.id
        ids.push(recipe.id)
        @recipes.push(recipe)
      end
    end
  end

end
