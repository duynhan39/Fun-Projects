class AthletesController < ApplicationController

  def index
    if params[:team]
      @athletes = Athlete.teammed_with(params[:team])
    else
      @athletes = Athlete.all
    end
  end

  def show
    @athlete = Athlete.find(params[:id])
  end

  def new
    @athlete = Athlete.new
  end

  def edit
    @athlete = Athlete.find(params[:id])
  end

  def create
    @athlete = Athlete.new(athlete_params)
    
    if @athlete.save
      redirect_to @athlete
    else
      render 'new'
    end
  
    #@athlete.save
    #redirect_to @athlete
  end
  
  def update
    @athlete = Athlete.find(params[:id])

    if @athlete.update(athlete_params)
      redirect_to @athlete
    else
      render 'edit'
    end
  end
  
  def destroy
    @athlete = Athlete.find(params[:id])
    @athlete.destroy
 
    redirect_to athletes_path
  end

  private

    def athlete_params
      params.require(:athlete).permit(
	      :name, 
	      :email, 
	      :phone) 
    end
end
