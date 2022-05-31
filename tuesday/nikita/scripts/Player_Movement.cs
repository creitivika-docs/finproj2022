using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;

public class Player_Movement : MonoBehaviour
{
    private Rigidbody2D rb;
    private Animator anim;
    private SpriteRenderer sprite;
    private BoxCollider2D coll;

    public ParticleSystem footsteps;
    private ParticleSystem.EmissionModule FootEmission;
    public ParticleSystem Confetti;
    public ParticleSystem Confetti2;
    public ParticleSystem Confetti3;

    public ParticleSystem FallEffect;
    private bool WasOnGround;

    private bool CheckpointActivated;
    private bool CheckpointActivated2;
    private bool CheckpointActivated3;
    
    [SerializeField] private LayerMask JumpableGround;

    [SerializeField] private Animator JumpPad;
    [SerializeField] private string Jump_Pad = "Jump_Pad";

    private float dirX = 0f;
    private float MoveSpeed = 12.5f;
    private float JumpForce = 28f;
    private float CoyoteTime = .15f;
    private float CoyoteTimeCounter;
    private float JumpBufferTime = .1f;
    private float JumpBufferCounter;
    public int deaths = 0;
    private enum MovementState { idle, walk, jump, jumpup }

    [SerializeField] private AudioSource audioSource;
    [SerializeField] private AudioClip DeathSoundEffect, JumpSoundEffect, CheckPointSoundEffect, JumpPadSoundEffect;

    [SerializeField] private Text deathsText;

    private Vector2 CurrentCheckPoint;

    private void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        sprite = GetComponent<SpriteRenderer>();
        anim = GetComponent<Animator>();
        coll = GetComponent<BoxCollider2D>();
        FootEmission = footsteps.emission;
        CurrentCheckPoint = transform.position;
    }

    private void Update()
    {

        dirX = Input.GetAxis("Horizontal");
        rb.velocity = new Vector2(dirX * MoveSpeed, rb.velocity.y);

        if(Input.GetAxis("Horizontal") != 0 && IsGrounded())
          {
            FootEmission.rateOverTime = 20f;
          }
        else
          {
            FootEmission.rateOverTime = 0f;
          }

        if(!WasOnGround && IsGrounded())
          {
            FallEffect.gameObject.SetActive(true);
            FallEffect.Stop();
            FallEffect.transform.position = footsteps.transform.position;
            FallEffect.Play();
          }

        WasOnGround = IsGrounded();

        if(IsGrounded())
          {
            CoyoteTimeCounter = CoyoteTime;

          }
        else
          {
            CoyoteTimeCounter -= Time.deltaTime;
          }

        if(Input.GetButtonDown("Jump"))
          {
            JumpBufferCounter = JumpBufferTime;
          }
        else
          {
            JumpBufferCounter -= Time.deltaTime;
          }

        if(CoyoteTimeCounter > 0f && JumpBufferCounter > 0f)
          {
            rb.velocity = new Vector2(rb.velocity.x, JumpForce);
          }

        if(CoyoteTimeCounter > 0f && JumpBufferCounter > 0f && !audioSource.isPlaying)
          {
            audioSource.pitch = Random.Range(0.75f, 1.25f);
            audioSource.PlayOneShot(JumpSoundEffect);
          }

        if(Input.GetButtonUp("Jump") && rb.velocity.y > 0f)
          {
            rb.velocity = new Vector2(rb.velocity.x, rb.velocity.y * .5f);
            CoyoteTimeCounter = 0f;
          }

        UpdateAnimationState();
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
      if(collision.gameObject.CompareTag("Trap"))
        {
          transform.position = CurrentCheckPoint;
          audioSource.pitch = Random.Range(0.5f, 2.5f);
          audioSource.PlayOneShot(DeathSoundEffect);
          deaths++;
          deathsText.text = "" + deaths;
        }
      if(collision.gameObject.CompareTag("Jump Pad"))
        {
          rb.velocity = new Vector2(rb.velocity.x, 37.5f);
          JumpPad.Play(Jump_Pad, 0, 0.0f);
          audioSource.pitch = Random.Range(1.5f, 2.5f);
          audioSource.PlayOneShot(JumpPadSoundEffect);
        }
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
      if (collision.gameObject.CompareTag("Secret"))
        {
          transform.position = new Vector2(1.375f, -11.89f); 
        }
      if (collision.gameObject.CompareTag("CheckPoint") && !CheckpointActivated)
        {
          CurrentCheckPoint = transform.position;
          CheckpointActivated = true;
          audioSource.pitch = Random.Range(0.85f, 1.15f);
          audioSource.PlayOneShot(CheckPointSoundEffect);
          Confetti.Play();
        }
      if (collision.gameObject.CompareTag("CheckPoint2") && !CheckpointActivated2)
        {
          CurrentCheckPoint = transform.position;
          CheckpointActivated2 = true;
          audioSource.pitch = Random.Range(0.85f, 1.15f);
          audioSource.PlayOneShot(CheckPointSoundEffect);
          Confetti2.Play();
        }
      if (collision.gameObject.CompareTag("CheckPoint3") && !CheckpointActivated3)
        {
          CurrentCheckPoint = transform.position;
          CheckpointActivated3 = true;
          audioSource.pitch = Random.Range(0.85f, 1.15f);
          audioSource.PlayOneShot(CheckPointSoundEffect);
          Confetti3.Play();
        }
    }

    private void UpdateAnimationState()
    {
        MovementState state;

        if(dirX > 0f)
          {
            state = MovementState.walk;
            sprite.flipX = false;
          }
        else if(dirX < 0f)
          {
            state = MovementState.walk;
            sprite.flipX = true;
          }
        else
          {
            state = MovementState.idle;
            sprite.flipX = false;
          }

        if(rb.velocity.y > .1f && dirX > 0f)
          {
            state = MovementState.jump;
            sprite.flipX = false;
          }
        else if(rb.velocity.y > .1f && dirX < 0f)
          {
            state = MovementState.jump;
            sprite.flipX = true;
          }
        else if(rb.velocity.y > .1f)
          {
            state = MovementState.jumpup;
          }

        anim.SetInteger("state", (int)state);
    }

    private bool IsGrounded()
    {
      return Physics2D.BoxCast(coll.bounds.center, coll.bounds.size, 0f, Vector2.down, .1f, JumpableGround);
    }
}