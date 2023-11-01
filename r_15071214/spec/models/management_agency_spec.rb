require 'rails_helper'

RSpec.describe ManagementAgency do
  describe '#create' do
    context '부모 관계인 NationalPoliceAgency와 PoliceStation를 미리 만들지 않아서' do
      let(:create_param) { { name: 'm_agency1', national_police_agency_id: 1, police_station_id: 1 } }
      let(:expected) { 'Validation failed: National police agency must exist, Police station must exist' }
      it 'create 불가능' do
        expect { ManagementAgency.create!(create_param) }.to raise_error(ActiveRecord::RecordInvalid, expected)
      end
    end

    context '부모 관계인 NationalPoliceAgency와 PoliceStation를 미리 만들면' do
      # NationalPoliceAgency
      let(:national_police_agency_id) { NationalPoliceAgency.create!({ name: 'p_agency1' }).id }
      # PoliceStation
      let(:police_station_id) { PoliceStation.create!({ name: 'p_station1', national_police_agency_id: }).id }
      # ManagementAgency
      let(:create_param) { { name: 'm_agency1', national_police_agency_id:, police_station_id: } }
      let(:expected) { 1 }
      it 'create 가능' do
        ManagementAgency.create!(create_param)
        actual = ManagementAgency.all.length

        expect(actual).to equal(expected)
      end
    end
  end
end
