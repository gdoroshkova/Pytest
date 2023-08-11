import pytest
import DQchecks


class TestCountries:
    @pytest.fixture()
    def value_for_countries_table(self):
        """Pass test data for inserting into hr.countries table"""
        values = ('BL', 'Belarus', '1')
        return values

    def test_countries_duplicates(self):
        """Duplicate check for hr.countries table.
        The check performs by calling check_duplicates function with
        'hr.countries', 'countries.country_id' parameters.
        The length of returned list should be equal 0."""
        result = DQchecks.check_duplicates('hr.countries', 'countries.country_id')
        assert len(result) == 0

    def test_countries_rows_amount(self, value_for_countries_table):
        """Check data completeness for hr.countries.
        1) Test calls check_amount_of_rows functon with hr.countries parameter
        that counts amount of rows in the table.
        2) Current function uses trn_db_connect fixture to return cursor
        and using it for inserting row into hr.countries table. Values for inserting are returned by
        value_for_countries_table fixture.
        3) After row inserting the test calls check_amount_of_rows again.
        4) Test compare amount of row before row inserting and amount after + 1.
        If the result is equal test is passed."""
        current_amount = DQchecks.check_amount_of_rows('hr.countries')
        parameters_list = DQchecks.get_db_settings('db_settings.txt')
        cursor = DQchecks.db_connection(parameters_list)
        cursor.execute(f"INSERT INTO hr.countries VALUES ('{value_for_countries_table[0]}', '{value_for_countries_table[1]}', '{value_for_countries_table[2]}')")
        changed_amount = DQchecks.check_amount_of_rows('hr.countries')
        assert current_amount + 1 == changed_amount
        cursor.execute(f"DELETE FROM hr.countries WHERE country_name='Belarus'")


class TestEmployees:
    def test_avg_salary_from_employees(self):
        """Check data completeness for hr.employees.salary column by finding average value.
        The check performs by calling check_avg_for_column function with
        'hr.employees', 'employees.salary' parameters.
        The returned result should be equal 8060.000000."""
        result = DQchecks.check_avg_for_column('hr.employees', 'employees.salary')
        assert result == 8060.000000

    def test_hiredate_from_employees(self):
        """Check correctness for employees.hire_date column by checking if date is in future or is null.
        The check performs by check_date_correctness function with
        'hr.employees', 'employees.hire_date' parameters.
        check_date_correctness function executes SELECT that returns date in future or null date.
        The length of returned list should be equal 0."""
        result = DQchecks.check_date_correctness('hr.employees', 'employees.hire_date')
        assert len(result) == 0


class TestLocations:

    def test_max_locid_from_locations(self):
        """Check data completeness for hr.locations.location_id column by finding max value.
        The check performs by calling check_max_for_column function with
        'hr.locations', 'locations.location_id' parameters.
        The returned result should be equal 2700."""
        result = DQchecks.check_max_for_column('hr.locations', 'locations.location_id')
        assert result == 2700

    # @pytest.mark.skip
    def test_postalcode_from_locations_for_null(self):
        """Check for NULL values locations.postal_code column by calling
        check_column_for_null_values function, that executes SELECT and return null values.
        Test is passed if the length of returned list should be equal 0."""
        result = DQchecks.check_column_for_null_values('hr.locations', 'locations.postal_code')
        assert len(result) == 0
