import pytest
import DQchecks


class TestCountries:
    @pytest.fixture()
    def value_for_countries_table(self):
        values = ('BL', 'Belarus', '1')
        return values

    @pytest.fixture()
    def trn_db_connect(self):
        cursor = DQchecks.db_connection('EPPLWROW03C4\\SQLEXPRESS', 'TRN', 'MyLogin', '123')
        return cursor

    def test_countries_duplicates(self):
        result = DQchecks.check_duplicates('hr.countries', 'countries.country_id')
        assert len(result) == 0

    def test_countries_rows_amount(self, value_for_countries_table, trn_db_connect):
        current_amount = DQchecks.check_amount_of_rows('hr.countries')
        cursor = trn_db_connect
        cursor.execute(f"INSERT INTO hr.countries VALUES ('{value_for_countries_table[0]}', '{value_for_countries_table[1]}', '{value_for_countries_table[2]}')")
        changed_amount = DQchecks.check_amount_of_rows('hr.countries')
        assert current_amount + 1 == changed_amount
        cursor.execute(f"DELETE FROM hr.countries WHERE country_name='Belarus'")


class TestEmployees:
    def test_avg_salary_from_employees(self):
        result = DQchecks.check_avg_for_column('hr.employees', 'employees.salary')
        assert result == 8060.000000

    def test_hiredate_from_employees(self):
        result = DQchecks.check_date_correctness('hr.employees', 'employees.hire_date')
        assert len(result) == 0


class TestLocations:

    def test_max_locid_from_locations(self):
        result = DQchecks.check_max_for_column('hr.locations', 'locations.location_id')
        assert result == 2700

    @pytest.mark.skip
    def test_postalcode_from_locations_for_null(self):
        result = DQchecks.check_column_for_null_values('hr.locations', 'locations.postal_code')
        assert len(result) == 0