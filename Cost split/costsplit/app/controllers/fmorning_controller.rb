class FmorningController < ApplicationController
  
  def new
    @fmorning = Fmorning.new
    @athletes = Athlete.all
  end

  def destroy
    @fmorning = Fmorning.find(params[:id])
    @fmorning.destroy
    redirect_to data_fmorning_data_path
  end
    
  def create
    @fmorning = Fmorning.new(fmorning_params)
    
    if @fmorning.save
      redirect_to @fmorning
    else
      @athletes = Athlete.all
      render 'new'
    end
  end

  def show
    @fmorning = Fmorning.find(params[:id])
  end

  private
  def fmorning_params
    params.require(:form).permit(:stdName,:urineCol,:sleepTime,:bodySoreness)
  end
  
end
