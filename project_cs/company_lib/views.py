from django.shortcuts import render, get_object_or_404
from .models import CompanyDetails

def company_list(request):
    # Fetch all companies
    companies = CompanyDetails.objects.all()

    # Fetch search query
    search_query = request.GET.get('search', None)

    # Apply search filter
    if search_query:
        companies = companies.filter(company_name__icontains=search_query)

    # Existing filters for country, year of founding, CET visited
    country_filter = request.GET.get('country', None)
    year_filter = request.GET.get('year', None)
    cet_visited_filter = request.GET.get('cet_visited', None)

    if country_filter:
        companies = companies.filter(country=country_filter)
    
    if cet_visited_filter:
        companies = companies.filter(college_visited=(cet_visited_filter == 'True'))

    if year_filter:
        year_range = year_filter.split('-')
        start_year = int(year_range[0])
        end_year = int(year_range[1])
        companies = companies.filter(founded__gte=start_year, founded__lte=end_year)

    # Define the specific 25-year ranges
    year_ranges = [
        '1970-1980', '1980-1990', '1990-2000', 
        '2000-2010', '2010-2020', '2020-2030'
    ]

    # Extract distinct values for country filter
    distinct_countries = companies.values_list('country', flat=True).distinct()

    context = {
        'companies': companies,
        'year_ranges': year_ranges,
        'distinct_countries': distinct_countries,
        'search_query': search_query,  # To retain the search query in the input field
    }

    return render(request, 'company_lib/company_list.html', context)


def company_detail(request, company_id):
    company = get_object_or_404(CompanyDetails, company_id=company_id)
    reviews = company.reviews.all()  # Fetch all reviews for the company
    context = {
        'company': company,
        'reviews': reviews,
    }
    return render(request, 'company_lib/company_detail.html', context)