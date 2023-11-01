require 'rails_helper'

RSpec.describe MultiUseFacility, type: :model do
  context '부모 관계인 Address와 MainPurpose를 미리 만들지 않아서' do
    let(:create_param) { { name: 'm_facility1', address_id: 1, main_purpose_id: 1 } }
    let(:expected) { 'Validation failed: Main purpose must exist, Address must exist' }
    it 'create 불가능' do
      expect { MultiUseFacility.create!(create_param) }.to raise_error(ActiveRecord::RecordInvalid, expected)
    end
  end

  context '부모 관계인 Address와 MainPurpose를 미리 만들면' do
    # Address
    let(:address_id) { Address.create!({ address: 'address1' }).id }
    # MainPurpose
    let(:main_purpose_id) { MainPurpose.create!({ purpose: 'purpose1' }).id }
    # MultiUseFacility
    let(:create_param) { { name: 'm_facility1', address_id:, main_purpose_id: } }
    let(:expected) { 1 }
    it 'create 가능' do
      MultiUseFacility.create!(create_param)
      actual = MultiUseFacility.all.length

      expect(actual).to equal(expected)
    end
  end
end
