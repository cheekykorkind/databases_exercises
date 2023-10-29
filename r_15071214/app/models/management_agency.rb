class ManagementAgency < ApplicationRecord
  belongs_to :national_police_agency
  belongs_to :police_station
  has_many :facility
end
