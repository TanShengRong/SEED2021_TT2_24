using API.Entities;
using Microsoft.EntityFrameworkCore;
namespace API.Data
{
    public class DataContext : DbContext
    {
        public DataContext(DbContextOptions options) : base(options)
        {
        }

        public DbSet<UserDetail> UserDetails { get; set; }
        public DbSet<LoginCredential> LoginCredentials { get; set; }
    }
}  