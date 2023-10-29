class PoliceStation < ApplicationRecord
  belongs_to :national_police_agency
  has_many :management_agency
end
