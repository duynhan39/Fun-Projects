module AthletesHelper
  def team_links(teams)
    teams.split(",").map{|team| link_to team.strip, team_path(team.strip)}.join(", ")
  end
end
