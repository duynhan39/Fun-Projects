class DataController < ApplicationController
  def index
  end

  def create
    render 'fmorning_data'
  end
  
  def fmorning_data
    @athletes = Athlete.all
    @fmorning = Fmorning.all
    respond_to do |format|
      format.html
      format.xlsx
    end
    
  end

  def factivity_data
    @athletes = Athlete.all
    @factivity = Factivity.all
    respond_to do |format|
      format.html
      format.xlsx
    end
  end
 
end
