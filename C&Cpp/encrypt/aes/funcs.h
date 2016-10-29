#ifndef _FUNCS_H_
#define _FUNCS_H_
static unsigned char s_box[256] = 
  "\x63\x7C\x77\x7B\xF2\x6B\x6F\xC5\x30\x01\x67\x2B\xFE\xD7\xAB\x76"
  "\xCA\x82\xC9\x7D\xFA\x59\x47\xF0\xAD\xD4\xA2\xAF\x9C\xA4\x72\xC0"
  "\xB7\xFD\x93\x26\x36\x3F\xF7\xCC\x34\xA5\xE5\xF1\x71\xD8\x31\x15"
  "\x04\xC7\x23\xC3\x18\x96\x05\x9A\x07\x12\x80\xE2\xEB\x27\xB2\x75"
  "\x09\x83\x2C\x1A\x1B\x6E\x5A\xA0\x52\x3B\xD6\xB3\x29\xE3\x2F\x84"
  "\x53\xD1\x00\xED\x20\xFC\xB1\x5B\x6A\xCB\xBE\x39\x4A\x4C\x58\xCF"
  "\xD0\xEF\xAA\xFB\x43\x4D\x33\x85\x45\xF9\x02\x7F\x50\x3C\x9F\xA8"
  "\x51\xA3\x40\x8F\x92\x9D\x38\xF5\xBC\xB6\xDA\x21\x10\xFF\xF3\xD2"
  "\xCD\x0C\x13\xEC\x5F\x97\x44\x17\xC4\xA7\x7E\x3D\x64\x5D\x19\x73"
  "\x60\x81\x4F\xDC\x22\x2A\x90\x88\x46\xEE\xB8\x14\xDE\x5E\x0B\xDB"
  "\xE0\x32\x3A\x0A\x49\x06\x24\x5C\xC2\xD3\xAC\x62\x91\x95\xE4\x79"
  "\xE7\xC8\x37\x6D\x8D\xD5\x4E\xA9\x6C\x56\xF4\xEA\x65\x7A\xAE\x08"
  "\xBA\x78\x25\x2E\x1C\xA6\xB4\xC6\xE8\xDD\x74\x1F\x4B\xBD\x8B\x8A"
  "\x70\x3E\xB5\x66\x48\x03\xF6\x0E\x61\x35\x57\xB9\x86\xC1\x1D\x9E"
  "\xE1\xF8\x98\x11\x69\xD9\x8E\x94\x9B\x1E\x87\xE9\xCE\x55\x28\xDF"
  "\x8C\xA1\x89\x0D\xBF\xE6\x42\x68\x41\x99\x2D\x0F\xB0\x54\xBB\x16"
  ;
static unsigned char rcon[256] =
  "\x8d\x01\x02\x04\x08\x10\x20\x40\x80\x1b\x36\x6c\xd8\xab\x4d\x9a"
  "\x2f\x5e\xbc\x63\xc6\x97\x35\x6a\xd4\xb3\x7d\xfa\xef\xc5\x91\x39"
  "\x72\xe4\xd3\xbd\x61\xc2\x9f\x25\x4a\x94\x33\x66\xcc\x83\x1d\x3a"
  "\x74\xe8\xcb\x8d\x01\x02\x04\x08\x10\x20\x40\x80\x1b\x36\x6c\xd8"
  "\xab\x4d\x9a\x2f\x5e\xbc\x63\xc6\x97\x35\x6a\xd4\xb3\x7d\xfa\xef"
  "\xc5\x91\x39\x72\xe4\xd3\xbd\x61\xc2\x9f\x25\x4a\x94\x33\x66\xcc"
  "\x83\x1d\x3a\x74\xe8\xcb\x8d\x01\x02\x04\x08\x10\x20\x40\x80\x1b"
  "\x36\x6c\xd8\xab\x4d\x9a\x2f\x5e\xbc\x63\xc6\x97\x35\x6a\xd4\xb3"
  "\x7d\xfa\xef\xc5\x91\x39\x72\xe4\xd3\xbd\x61\xc2\x9f\x25\x4a\x94"
  "\x33\x66\xcc\x83\x1d\x3a\x74\xe8\xcb\x8d\x01\x02\x04\x08\x10\x20"
  "\x40\x80\x1b\x36\x6c\xd8\xab\x4d\x9a\x2f\x5e\xbc\x63\xc6\x97\x35"
  "\x6a\xd4\xb3\x7d\xfa\xef\xc5\x91\x39\x72\xe4\xd3\xbd\x61\xc2\x9f"
  "\x25\x4a\x94\x33\x66\xcc\x83\x1d\x3a\x74\xe8\xcb\x8d\x01\x02\x04"
  "\x08\x10\x20\x40\x80\x1b\x36\x6c\xd8\xab\x4d\x9a\x2f\x5e\xbc\x63"
  "\xc6\x97\x35\x6a\xd4\xb3\x7d\xfa\xef\xc5\x91\x39\x72\xe4\xd3\xbd"
  "\x61\xc2\x9f\x25\x4a\x94\x33\x66\xcc\x83\x1d\x3a\x74\xe8\xcb\x8d"
  ;
static unsigned char* keys ;
void test( ) ;
void print_4x4_matrix( unsigned char* state ) ;
void sub_bytes( unsigned char* state ) ;
void shift_rows( unsigned char* state ) ;
void mix_columns( unsigned char* state ) ;
void generate_keys( unsigned char* passphrase ) ;
void add_round_key( unsigned char* in , int round ) ;
#endif
