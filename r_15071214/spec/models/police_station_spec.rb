require 'rails_helper'

RSpec.describe PoliceStation do
  describe '#create' do
    context '부모 관계인 NationalPoliceAgency를 미리 만들지 않아서' do
      let(:create_param) { { name: 'p_station1', national_police_agency_id: 1 } }
      let(:expected) { 'Validation failed: National police agency must exist' }
      it 'create 불가능' do
        expect { PoliceStation.create!(create_param) }.to raise_error(ActiveRecord::RecordInvalid, expected)
      end
    end

    context '부모 관계인 NationalPoliceAgency를 미리 만들면' do
      # NationalPoliceAgency
      let(:national_police_agency_id) { NationalPoliceAgency.create!({ name: 'p_agency1' }).id }

      # PoliceStation
      let(:create_param) { { name: 'p_station1', national_police_agency_id: } }
      let(:expected) { 1 }
      it 'create 가능' do
        PoliceStation.create!(create_param)
        actual = PoliceStation.all.length

        expect(actual).to equal(expected)
      end
    end
  end
end
