class NationalPoliceAgency < ApplicationRecord
  has_many :police_station
  has_many :management_agency
end
