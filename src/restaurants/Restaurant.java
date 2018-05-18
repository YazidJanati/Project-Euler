package restaurants;
import java.util.HashSet;

import org.codehaus.jackson.annotate.JsonIgnore;
import org.codehaus.jackson.annotate.JsonProperty;

public class Restaurant {
	@JsonProperty
	String business_id;
	@JsonProperty
	public String name;
	@JsonProperty
	String neighborhood;
	@JsonProperty
	String address;
	@JsonProperty
	String city;
	@JsonProperty
	String state;
	@JsonProperty
	String postal_code;
	@JsonProperty
	public Double latitude;
	@JsonProperty
	public Double longitude;
	@JsonProperty
	Double stars;
	@JsonProperty
	public HashSet<String> categories;
	@JsonProperty
	Double review_count;
	@JsonProperty
	Boolean is_open;
	@JsonIgnore
	double note;
	@JsonIgnore
	public Spécialité spécialité;

	public Restaurant(){}

	public Restaurant(double latitude,double longitude) {
		this.latitude=latitude;
		this.longitude=longitude;
	}

	public String toString() {
		return "Name:"+" "+name+" / "+"Address:"+" "+address+" / "+"Stars:"+" "+stars+" / "+" Category:"+category(categories);
	}

	public String getBusiness_id() {
		return business_id;
	}

	public String getName() {
		return name;
	}

	public String getNeighborhood() {
		return neighborhood;
	}

	public String getAddress() {
		return address;
	}
	public HashSet<String> getCategories() {
		return categories;
	}

	public String getCity() {
		return city;
	}

	public String getState() {
		return state;
	}
	
	public Spécialité getSpécialité() {
		return spécialité;
	}

	public String getPostal_code() {
		return postal_code;
	}

	public Double getLatitude() {
		return latitude;
	}

	public Double getLongitude() {
		return longitude;
	}

	public Double getStars() {
		return stars;
	}

	public Double getReview_count() {
		return review_count;
	}

	public Boolean getIs_open() {
		return is_open;
	}

	public double getNote() {
		return note;
	}

	public void setBusiness_id(String business_id) {
		this.business_id = business_id;
	}

	public void setName(String name) {
		this.name = name;
	}

	public void setNeighborhood(String neighborhood) {
		this.neighborhood = neighborhood;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public void setState(String state) {
		this.state = state;
	}

	public void setPostal_code(String postal_code) {
		this.postal_code = postal_code;
	}

	public void setLatitude(Double latitude) {
		this.latitude = latitude;
	}

	public void setLongitude(Double longitude) {
		this.longitude = longitude;
	}

	public void setStars(Double stars) {
		this.stars = stars;
	}

	public void setReview_count(Double review_count) {
		this.review_count = review_count;
	}

	public void setIs_open(Boolean is_open) {
		this.is_open = is_open;
	}

	public void setNote(double note) {
		this.note = note;
	}
	public String category(HashSet<String> liste) {
		String a=" ";
		for (String word: liste) {
			a+=word+", ";
		}
		return a;
	}



}

